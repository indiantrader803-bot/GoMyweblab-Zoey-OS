from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import sqlite3
import os
import urllib.parse
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "autonomous-org-dashboard"))
DB_PATH = os.path.join(BASE_DIR, "..", "data", "gomyweblab_state.db")
FREELANCE_DB = os.path.join(BASE_DIR, "..", "data", "freelance_pipeline.db")
POLICY_PATH = os.path.join(BASE_DIR, "..", "config", "gomyweblab_policy.json")

sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "..", "connectors"))
import auth_manager
from live_trading_bridge import LiveTradingBridge

# Initialize Zoey multi-core modules (zoey-ferbin-core memory + autonomous-org-core zoey)
FERBIN_CORE_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "..", "zoey-ferbin-core"))
if os.path.exists(FERBIN_CORE_DIR) and FERBIN_CORE_DIR not in sys.path:
    sys.path.insert(0, FERBIN_CORE_DIR)

try:
    import zoey
    org_zoey_dir = os.path.abspath(os.path.join(BASE_DIR, "..", "zoey"))
    if org_zoey_dir not in getattr(zoey, '__path__', []):
        zoey.__path__.append(org_zoey_dir)
except Exception:
    pass

sys.path.append(os.path.join(BASE_DIR, "..", "zoey"))
from zoey_orchestrator import ZoeyOrchestrator
from daily_reporter import DailyReporter
from incident_manager import IncidentManager
from telephony_bridge import TelephonyBridge

zoey_orchestrator = ZoeyOrchestrator()
daily_reporter = DailyReporter()
incident_manager = IncidentManager()
telephony_bridge = TelephonyBridge()


trading_bridge = LiveTradingBridge()

sys.path.append(os.path.join(BASE_DIR, "..", "freelance_engine"))
from orchestrator import FullLifecycleFreelanceOrchestrator
from gomyweblab_director import GomyweblabDirector

director = GomyweblabDirector()
freelance_orch = FullLifecycleFreelanceOrchestrator()

# Session in-memory store
SESSIONS = set()

class GomyweblabHttpHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DASHBOARD_DIR, **kwargs)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8') if content_len > 0 else '{}'
        data = json.loads(body) if body else {}

        # 1. User Registration
        if parsed.path == "/api/register":
            username = data.get('username', '').strip()
            email = data.get('email', '').strip()
            password = data.get('password', '').strip()

            if not username or not password or not email:
                self.send_json({"error": "Username, email, and password are required."}, 400)
                return

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            try:
                pw_hash = auth_manager.hash_pw(password)
                cur.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
                            (username, email, pw_hash))
                conn.commit()
                token = auth_manager.secrets.token_hex(24)
                SESSIONS.add(token)
                self.send_json({"success": True, "token": token, "username": username, "role": "admin"})
            except sqlite3.IntegrityError:
                self.send_json({"error": "Username or Email already registered."}, 409)
            finally:
                conn.close()
            return

        # 2. User Login
        elif parsed.path == "/api/zoey/ask":
            # parsed above
            prompt = data.get("prompt", "")
            res = zoey_orchestrator.ask_zoey(prompt)
            self.send_json(res)
            return

        elif parsed.path == "/api/zoey/approval/action":
            # parsed above
            apv_id = data.get("id")
            decision = data.get("decision", "APPROVED")
            res = zoey_orchestrator.resolve_approval(apv_id, decision)
            self.send_json(res)
            return

        elif parsed.path == "/api/zoey/incident/resolve":
            # parsed above
            inc_id = data.get("id")
            res = incident_manager.resolve_incident(inc_id)
            self.send_json(res)
            return

        elif parsed.path == "/api/zoey/telephony/test-call":
            # parsed above
            res = telephony_bridge.trigger_p0_call(
                "INC-TEST-VOICE", "Simulated P0 Critical Outage", "Infrastructure",
                "Simulated high-priority test event", "Acknowledge in dashboard"
            )
            self.send_json(res)
            return

        elif parsed.path == "/api/login":
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id, username, password_hash, role FROM users WHERE username = ? OR email = ?",
                        (username, username))
            user = cur.fetchone()
            conn.close()

            if user and auth_manager.verify_pw(password, user[2]):
                token = auth_manager.secrets.token_hex(24)
                SESSIONS.add(token)
                self.send_json({"success": True, "token": token, "username": user[1], "role": user[3]})
            else:
                self.send_json({"error": "Invalid username or password credentials."}, 401)
            return

        # 3. Agent Heartbeat / Ping (Proof of 24/7 Activity)
        elif parsed.path == "/api/agent-heartbeat":
            agent_id = data.get('agent_id')
            api_key = data.get('api_key')

            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id FROM agents WHERE id = ? AND api_key = ?", (agent_id, api_key))
            ag = cur.fetchone()

            if ag:
                cur.execute("""
                    UPDATE agents 
                    SET last_heartbeat = CURRENT_TIMESTAMP, 
                        daily_active_status = 'ACTIVE_ONLINE'
                    WHERE id = ?
                """, (agent_id,))
                cur.execute("""
                    INSERT INTO agent_daily_heartbeats (agent_id, activity_type, status)
                    VALUES (?, 'MANUAL_PING_HEARTBEAT', 'ACTIVE_OK')
                """, (agent_id,))
                conn.commit()
                self.send_json({"success": True, "status": "ACTIVE_VERIFIED", "timestamp": str(datetime.now())})
            else:
                self.send_json({"error": "Invalid Agent API Key."}, 403)
            conn.close()
            return

        return super().do_POST()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)

        # Handle page routes
        if parsed.path in ["/admin", "/admin/", "/dashboard", "/dashboard/"]:
            self.path = "/admin.html"
            return super().do_GET()
        elif parsed.path in ["/grok", "/grok/"]:
            self.path = "/index.html"
            return super().do_GET()
        elif parsed.path in ["/trading", "/trading/"]:
            self.path = "/index.html"
            return super().do_GET()
        elif parsed.path in ["/workflows", "/workflows/"]:
            self.path = "/index.html"
            return super().do_GET()

        # 1. Agent Daily Activity & Credentials Roster
        if parsed.path == "/api/agents-roster":
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                SELECT id, name, swarm_id, role, tag, api_key, agent_email, credential_secret,
                       daily_active_status, consecutive_active_days, uptime_percentage,
                       last_heartbeat, shift_schedule, tasks_completed,
                       current_task_title, task_progress_pct, task_time_spent, task_est_remaining, active_subtask
                FROM agents ORDER BY swarm_id, name
            """)
            agents = [{
                "id": r[0], "name": r[1], "swarm": r[2], "role": r[3], "tag": r[4],
                "api_key": r[5], "email": r[6], "secret": r[7], "daily_status": r[8],
                "consecutive_days": r[9], "uptime": f"{r[10]:.1f}%",
                "last_heartbeat": r[11] or "Just Now", "shift": r[12], "completed": r[13],
                "task_title": r[14] or "Processing autonomous queue",
                "progress": r[15] if r[15] is not None else 75,
                "time_spent": r[16] or "25m",
                "est_remaining": r[17] or "10m",
                "subtask": r[18] or "Executing background routine"
            } for r in cur.fetchall()]

            # Fetch recent heartbeats
            cur.execute("""
                SELECT h.agent_id, a.name, h.heartbeat_time, h.activity_type, h.status
                FROM agent_daily_heartbeats h
                JOIN agents a ON h.agent_id = a.id
                ORDER BY h.id DESC LIMIT 15
            """)
            heartbeats = [{
                "agent_id": r[0], "name": r[1], "time": r[2], "type": r[3], "status": r[4]
            } for r in cur.fetchall()]
            conn.close()

            self.send_json({"agents": agents, "heartbeats": heartbeats})
            return

        # 2. General Org Status & Revenue Breakdown
        elif parsed.path == "/api/status":
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM tasks")
            total_tasks = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM tasks WHERE status = 'completed'")
            completed_tasks = cur.fetchone()[0]

            cur.execute("SELECT COUNT(*) FROM agents WHERE daily_active_status LIKE '%ACTIVE%'")
            active_agents = cur.fetchone()[0]

            # Real Financial Ledger Calculations
            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'RELEASED_EARNED'")
            total_earned = cur.fetchone()[0]

            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'ESCROW_LOCKED'")
            in_escrow = cur.fetchone()[0]

            cur.execute("SELECT id, transaction_ref, client_name, project_title, platform, amount_usd, payment_status, created_at FROM financial_ledger ORDER BY id DESC LIMIT 5")
            transactions = [{
                "id": r[0], "ref": r[1], "client": r[2], "title": r[3], "platform": r[4], "amount": r[5], "status": r[6], "date": r[7]
            } for r in cur.fetchall()]

            conn.close()

            with open(POLICY_PATH, "r", encoding="utf-8") as f:
                policy = json.load(f)

            # Live Trading Bridge Sync
            trading_stats = trading_bridge.get_live_market_stats()

            self.send_json({
                "organization": policy.get("organization_name"),
                "tagline": policy.get("tagline"),
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks,
                "active_swarms": 5,
                "online_agents": active_agents,
                "trading": trading_stats,
                "revenue": {
                    "total_earned_usd": total_earned,
                    "in_escrow_usd": in_escrow,
                    "pipeline_pending_usd": 0.0,
                    "currency": "USD",
                    "recent_transactions": transactions
                },
                "policy": policy
            })
            return

        # 3. Freelance Pipeline
        elif parsed.path == "/api/freelance-pipeline":
            fconn = sqlite3.connect(FREELANCE_DB)
            fcur = fconn.cursor()
            fcur.execute("""
                SELECT deal_ref, platform, client_name, client_country, project_title,
                       client_budget, market_benchmark_rate, negotiated_budget, current_stage,
                       demo_url, client_feedback, handover_repo, confidence_score, updated_at
                FROM freelance_deals ORDER BY id DESC
            """)
            deals = [{
                "ref": r[0], "platform": r[1], "client": r[2], "country": r[3], "title": r[4],
                "client_budget": r[5], "benchmark": r[6], "negotiated": r[7], "stage": r[8],
                "demo_url": r[9], "feedback": r[10], "handover": r[11], "confidence": f"{r[12]:.1%}", "updated": r[13]
            } for r in fcur.fetchall()]

            fcur.execute("SELECT deal_ref, sender, message_text, intent, decision_applied, timestamp FROM client_conversations ORDER BY id DESC LIMIT 10")
            messages = [{
                "deal": r[0], "sender": r[1], "text": r[2], "intent": r[3], "decision": r[4], "time": r[5]
            } for r in fcur.fetchall()]
            fconn.close()

            # Retrieve real-time background task telemetry
            b_tasks = []
            try:
                conn_b = sqlite3.connect(DB_PATH)
                cur_b = conn_b.cursor()
                cur_b.execute("""
                    SELECT task_name, agent_name, category, status, details, progress_pct, last_run_at
                    FROM live_background_tasks ORDER BY id DESC LIMIT 15
                """)
                b_tasks = [{
                    "task": row[0], "agent": row[1], "category": row[2], "status": row[3],
                    "details": row[4], "progress": row[5], "time": row[6]
                } for row in cur_b.fetchall()]
                conn_b.close()
            except Exception:
                pass

            self.send_json({"deals": deals, "messages": messages, "live_background_tasks": b_tasks})
            return

        # 4. Trigger Autonomous Cycle
        elif parsed.path == "/api/trigger-cycle":
            org_result = director.run_cycle()
            freelance_step = freelance_orch.run_lifecycle_step()

            # Record automated agent heartbeat for active agents
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
                UPDATE agents 
                SET last_heartbeat = CURRENT_TIMESTAMP, 
                    daily_active_status = 'ACTIVE_ONLINE'
            """)
            conn.commit()
            conn.close()

            self.send_json({
                "org": org_result,
                "freelance": freelance_step,
                "timestamp": org_result.get("time")
            })
            return

        # 4c. ZOEY AI COMMAND CENTER ENDPOINTS
        elif parsed.path == "/api/zoey/overview":
            status_data = trading_bridge.get_live_market_stats()
            latest_report = daily_reporter.get_latest_report()
            incidents = incident_manager.list_incidents(5)
            roster = zoey_orchestrator.get_specialist_roster()
            
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT count(*) FROM zoey_approvals WHERE status = 'PENDING'")
            pending_approvals = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM tasks WHERE status = 'completed'")
            completed_tasks = cur.fetchone()[0]
            cur.execute("SELECT count(*) FROM tasks WHERE status != 'completed'")
            overdue_tasks = cur.fetchone()[0]
            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'RELEASED_EARNED'")
            total_earned = cur.fetchone()[0]
            conn.close()

            self.send_json({
                "status": "ONLINE",
                "coo": "Zoey AI",
                "specialist_agents_count": len(roster),
                "workforce_agents_count": 20,
                "total_earned_usd": total_earned,
                "pending_approvals": pending_approvals,
                "completed_tasks": completed_tasks,
                "overdue_tasks": overdue_tasks,
                "active_incidents": len([i for i in incidents if i['status'] != 'RESOLVED']),
                "recent_incidents": incidents,
                "latest_report": latest_report,
                "timestamp": datetime.now().isoformat()
            })
            return

        elif parsed.path == "/api/zoey/employees":
            self.send_json({
                "specialists": zoey_orchestrator.get_specialist_roster()
            })
            return

        elif parsed.path == "/api/zoey/daily-report":
            report = daily_reporter.get_latest_report()
            self.send_json(report)
            return

        elif parsed.path == "/api/zoey/incidents":
            self.send_json({
                "incidents": incident_manager.list_incidents(20)
            })
            return

        elif parsed.path == "/api/zoey/approvals":
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id, requested_action, requesting_agent, business_reason, expected_result, risk_level, related_record, proposed_payload, status, created_at FROM zoey_approvals ORDER BY created_at DESC")
            approvals = [{
                "id": r[0], "action": r[1], "agent": r[2], "reason": r[3], "result": r[4], "risk": r[5],
                "record": r[6], "payload": r[7], "status": r[8], "date": r[9]
            } for r in cur.fetchall()]
            conn.close()
            self.send_json({"approvals": approvals})
            return

        elif parsed.path == "/api/zoey/memory":
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT id, category, key_name, content, confidence, updated_at FROM zoey_memory ORDER BY id ASC")
            memories = [{
                "id": r[0], "category": r[1], "key": r[2], "content": r[3], "confidence": r[4], "updated": r[5]
            } for r in cur.fetchall()]
            conn.close()
            self.send_json({"memories": memories})
            return

        elif parsed.path == "/api/zoey/telephony-history":
            self.send_json({
                "logs": telephony_bridge.get_telephony_history(20)
            })
            return

        # 4b. Real Financial Ledger & Earned Revenue Endpoint
        elif parsed.path == "/api/financial-ledger":
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'RELEASED_EARNED'")
            total_earned = cur.fetchone()[0]
            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'ESCROW_LOCKED'")
            in_escrow = cur.fetchone()[0]
            cur.execute("""
                SELECT id, transaction_ref, deal_ref, client_name, project_title, platform, amount_usd, payment_status, released_at, created_at 
                FROM financial_ledger 
                ORDER BY id DESC
            """)
            ledger_items = [{
                "id": r[0], "ref": r[1], "deal_ref": r[2], "client": r[3], "title": r[4], 
                "platform": r[5], "amount": r[6], "status": r[7], "released_at": r[8], "date": r[9]
            } for r in cur.fetchall()]
            conn.close()

            self.send_json({
                "status": "SUCCESS",
                "total_earned_usd": total_earned,
                "in_escrow_usd": in_escrow,
                "currency": "USD",
                "upi_settlement": "8240438062@superyes",
                "director": "Arnab",
                "ledger": ledger_items
            })
            return

        # 5. Open Source Alternatives Catalog
        elif parsed.path == "/api/open-source-alternatives":
            json_path = os.path.join(os.path.dirname(__file__), "..", "data", "open_source_alternatives.json")
            if os.path.exists(json_path):
                with open(json_path, "r", encoding="utf-8") as f:
                    alternatives_data = json.load(f)
                self.send_json({
                    "status": "SUCCESS",
                    "total_categories": len(alternatives_data),
                    "total_tools": sum(len(c.get("tools", [])) for c in alternatives_data),
                    "categories": alternatives_data
                })
            else:
                self.send_json({"status": "NOT_FOUND", "categories": []}, status=404)
            return

        # 6. Razorpay Payouts Gateway Status & Execution
        elif parsed.path == "/api/razorpay-status":
            from razorpay_bridge import RazorpayPayoutEngine
            rp = RazorpayPayoutEngine()
            self.send_json(rp.get_status())
            return

        # 7. Hermes Agent Integration Status & Execution
        elif parsed.path == "/api/hermes-status":
            import hermes_bridge
            self.send_json(hermes_bridge.get_hermes_status())
            return

        # 8. Actionsflow Alternative Engine Status & Workflow Trigger
        elif parsed.path == "/api/actionsflow-status":
            import actionsflow_bridge
            self.send_json(actionsflow_bridge.get_actionsflow_status())
            return

        return super().do_GET()

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

def run_server(port=8088):
    server = HTTPServer(('127.0.0.1', port), GomyweblabHttpHandler)
    print(f"Gomyweblab Server serving at http://127.0.0.1:{port}")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
