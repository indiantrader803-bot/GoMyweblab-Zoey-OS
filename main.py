"""
WSGI / ASGI Production Bridge for GoMyweblab & Zoey AI on Render
Runs 24/7 in the cloud:
- Bootstraps and protects SQLite State DB & Freelance Pipeline DB
- Runs Background Autonomous Agent Loop:
  * Freelance Scout: discovers high-ticket gigs on Upwork, Fiverr, and Freelancer
  * Pricing & Proposal Bot: sends automated proposals with benchmark pricing
  * Negotiation Bot: locks in milestone contracts & escrow
  * Autonomous Builder: tests and prepares delivery previews
  * Handover & Invoicing: updates real earned ledger
"""

import os
import sys
import time
import sqlite3
import threading

# Add core and zoey paths
CORE_DIR = os.path.join(os.path.dirname(__file__), "autonomous-org-core")
AGENTS_DIR = os.path.join(CORE_DIR, "agents")
ZOEY_DIR = os.path.join(CORE_DIR, "zoey")
FREELANCE_DIR = os.path.join(CORE_DIR, "freelance_engine")
DATA_DIR = os.path.join(CORE_DIR, "data")

DB_PATH = os.path.join(DATA_DIR, "gomyweblab_state.db")
FREELANCE_DB_PATH = os.path.join(DATA_DIR, "freelance_pipeline.db")
SQL_DUMP_PATH = os.path.join(DATA_DIR, "schema.sql")
FREELANCE_SQL_PATH = os.path.join(DATA_DIR, "freelance_schema.sql")

sys.path.append(CORE_DIR)
sys.path.append(AGENTS_DIR)
sys.path.append(ZOEY_DIR)
sys.path.append(FREELANCE_DIR)

def ensure_database():
    os.makedirs(DATA_DIR, exist_ok=True)
    # 1. State DB
    if os.path.exists(SQL_DUMP_PATH):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='tasks'")
        has_tasks = cur.fetchone()[0]
        if has_tasks == 0:
            print("[Init] Bootstrapping state database from schema.sql...")
            with open(SQL_DUMP_PATH, "r", encoding="utf-8") as f:
                cur.executescript(f.read())
            conn.commit()
            print("[Init] State database bootstrap complete.")
        conn.close()

    # 2. Freelance Pipeline DB
    if os.path.exists(FREELANCE_SQL_PATH):
        conn = sqlite3.connect(FREELANCE_DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='freelance_deals'")
        has_deals = cur.fetchone()[0]
        if has_deals == 0:
            print("[Init] Bootstrapping freelance pipeline from freelance_schema.sql...")
            with open(FREELANCE_SQL_PATH, "r", encoding="utf-8") as f:
                cur.executescript(f.read())
            conn.commit()
            print("[Init] Freelance pipeline bootstrap complete.")
        conn.close()

def run_autonomous_agent_worker():
    """Background worker daemon running 24/7 on the cloud server using the Unified Best-in-Class Engine."""
    print("[AutonomousWorker] 24/7 Unified Best-in-Class Agent Daemon starting...")
    time.sleep(5)  # initial wait for server bind
    try:
        from unified_engine import UnifiedFreelanceEngine
        unified_engine = UnifiedFreelanceEngine()
    except Exception as e:
        print(f"[AutonomousWorker] Error importing unified engine: {e}")
        return

    while True:
        try:
            # Single non-overlapping unified execution cycle
            report = unified_engine.run_unified_cycle()
            print(f"[AutonomousWorker] Unified Cycle Success -> Upwork: {report.get('upwork_deals_staged')} | Freelancer: {report.get('freelancer_bids_staged')} | Bounties: {report.get('web3_bounties_staged')}")
        except Exception as err:
            print(f"[AutonomousWorker] Unified Loop Error: {err}")

        # Run cleanly every 60 seconds autonomously in background
        time.sleep(60)

from server import GomyweblabHttpHandler
from http.server import HTTPServer

def run_app():
    ensure_database()
    
    # Start 24/7 background agent loop thread
    worker_thread = threading.Thread(target=run_autonomous_agent_worker, daemon=True)
    worker_thread.start()

    port = int(os.environ.get("PORT", 8088))
    server = HTTPServer(('0.0.0.0', port), GomyweblabHttpHandler)
    print(f"GoMyWebLab & Zoey OS Live Server listening on 0.0.0.0:{port}")
    server.serve_forever()

if __name__ == '__main__':
    run_app()
