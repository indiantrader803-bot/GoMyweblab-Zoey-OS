"""
WSGI / ASGI Production Bridge for GoMyweblab & Zoey AI on Render
"""

import os
import sys
import sqlite3

# Add core and zoey paths
CORE_DIR = os.path.join(os.path.dirname(__file__), "autonomous-org-core")
AGENTS_DIR = os.path.join(CORE_DIR, "agents")
ZOEY_DIR = os.path.join(CORE_DIR, "zoey")
DATA_DIR = os.path.join(CORE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "gomyweblab_state.db")
SQL_DUMP_PATH = os.path.join(DATA_DIR, "schema.sql")

sys.path.append(CORE_DIR)
sys.path.append(AGENTS_DIR)
sys.path.append(ZOEY_DIR)

def ensure_database():
    os.makedirs(DATA_DIR, exist_ok=True)
    if os.path.exists(SQL_DUMP_PATH):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='tasks'")
        has_tasks = cur.fetchone()[0]
        if has_tasks == 0:
            print("Bootstrapping database from schema.sql...")
            with open(SQL_DUMP_PATH, "r", encoding="utf-8") as f:
                cur.executescript(f.read())
            conn.commit()
            print("Database bootstrap complete.")
        conn.close()

from server import GomyweblabHttpHandler
from http.server import HTTPServer

def run_app():
    ensure_database()
    port = int(os.environ.get("PORT", 8088))
    server = HTTPServer(('0.0.0.0', port), GomyweblabHttpHandler)
    print(f"GoMyWebLab & Zoey OS Live Server listening on 0.0.0.0:{port}")
    server.serve_forever()

if __name__ == '__main__':
    run_app()
