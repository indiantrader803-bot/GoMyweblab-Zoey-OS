import sys
import os

# Add zoey directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), "zoey"))
from zoey_orchestrator import ZoeyOrchestrator
from daily_reporter import DailyReporter
from incident_manager import IncidentManager
from telephony_bridge import TelephonyBridge

with open('autonomous-org-core/agents/server.py', 'r', encoding='utf-8') as f:
    code = f.read()

# Add imports and instances at top
top_import_target = "from live_trading_bridge import LiveTradingBridge"
zoey_init_code = """from live_trading_bridge import LiveTradingBridge
sys.path.append(os.path.join(BASE_DIR, "..", "zoey"))
from zoey_orchestrator import ZoeyOrchestrator
from daily_reporter import DailyReporter
from incident_manager import IncidentManager
from telephony_bridge import TelephonyBridge

zoey_orchestrator = ZoeyOrchestrator()
daily_reporter = DailyReporter()
incident_manager = IncidentManager()
telephony_bridge = TelephonyBridge()
"""

if top_import_target in code and "zoey_orchestrator = ZoeyOrchestrator()" not in code:
    code = code.replace(top_import_target, zoey_init_code)
    print("Added Zoey orchestrator initializations to server.py")

# Add Zoey endpoints to do_GET
get_target = '        # 4b. Real Financial Ledger & Earned Revenue Endpoint'
zoey_get_endpoints = """        # 4c. ZOEY AI COMMAND CENTER ENDPOINTS
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

        # 4b. Real Financial Ledger & Earned Revenue Endpoint"""

if get_target in code and '/api/zoey/overview' not in code:
    code = code.replace(get_target, zoey_get_endpoints)
    print("Added Zoey GET endpoints to server.py")

# Add Zoey endpoints to do_POST
post_target = '        elif parsed.path == "/api/login":'
zoey_post_endpoints = """        elif parsed.path == "/api/zoey/ask":
            data = self.read_json_body()
            prompt = data.get("prompt", "")
            res = zoey_orchestrator.ask_zoey(prompt)
            self.send_json(res)
            return

        elif parsed.path == "/api/zoey/approval/action":
            data = self.read_json_body()
            apv_id = data.get("id")
            decision = data.get("decision", "APPROVED")
            res = zoey_orchestrator.resolve_approval(apv_id, decision)
            self.send_json(res)
            return

        elif parsed.path == "/api/zoey/incident/resolve":
            data = self.read_json_body()
            inc_id = data.get("id")
            res = incident_manager.resolve_incident(inc_id)
            self.send_json(res)
            return

        elif parsed.path == "/api/zoey/telephony/test-call":
            data = self.read_json_body()
            res = telephony_bridge.trigger_p0_call(
                "INC-TEST-VOICE", "Simulated P0 Critical Outage", "Infrastructure",
                "Simulated high-priority test event", "Acknowledge in dashboard"
            )
            self.send_json(res)
            return

        elif parsed.path == "/api/login":"""

if post_target in code and '/api/zoey/ask' not in code:
    code = code.replace(post_target, zoey_post_endpoints)
    print("Added Zoey POST endpoints to server.py")

with open('autonomous-org-core/agents/server.py', 'w', encoding='utf-8') as f:
    f.write(code)
print("Updated server.py written successfully.")
