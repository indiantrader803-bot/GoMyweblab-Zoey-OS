import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "gomyweblab_state.db")

def init_zoey_tables():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS zoey_incidents (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        severity TEXT NOT NULL,
        department TEXT NOT NULL,
        source TEXT NOT NULL,
        business_impact TEXT NOT NULL,
        responsible_manager TEXT,
        recommended_action TEXT,
        status TEXT DEFAULT 'OPEN',
        acknowledged_at DATETIME,
        resolved_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS zoey_approvals (
        id TEXT PRIMARY KEY,
        requested_action TEXT NOT NULL,
        requesting_agent TEXT NOT NULL,
        business_reason TEXT NOT NULL,
        expected_result TEXT,
        risk_level TEXT NOT NULL,
        related_record TEXT,
        proposed_payload TEXT,
        status TEXT DEFAULT 'PENDING',
        reviewed_by TEXT,
        reviewed_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS zoey_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        key_name TEXT NOT NULL,
        content TEXT NOT NULL,
        confidence REAL DEFAULT 1.0,
        source TEXT,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS zoey_daily_reports (
        id TEXT PRIMARY KEY,
        report_date TEXT NOT NULL,
        timezone TEXT DEFAULT 'Asia/Kolkata',
        executive_overview TEXT,
        employee_summary TEXT,
        project_performance TEXT,
        department_performance TEXT,
        sales_report TEXT,
        marketing_report TEXT,
        finance_summary TEXT,
        critical_issues TEXT,
        tomorrow_priorities TEXT,
        raw_json TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS zoey_telephony_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident_id TEXT,
        recipient_phone TEXT,
        channel TEXT,
        provider TEXT,
        status TEXT,
        dtmf_input TEXT,
        response_payload TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Seed baseline persistent memory if empty
    cur.execute("SELECT count(*) FROM zoey_memory")
    if cur.fetchone()[0] == 0:
        memories = [
            ("POLICY", "operating_hours", "24/7 continuous autonomous agency operation; daily reports delivered at 6:00 PM IST."),
            ("POLICY", "approval_thresholds", "Actions requiring approval: external emails, publishing public content, financial disbursements, production deployments."),
            ("DIRECTOR", "contact_info", "Director Arnab; UPI settlement destination: 8240438062@superyes; Emergency voice call priority recipient."),
            ("CAPITAL", "exchange_allocation", "Multi-exchange capital pool: Delta Exchange India ($1,000 USDT), CoinSwitch ($1,010 USDT), Coinbase CDP ($500 USDT). Total: $2,510 USDT."),
            ("WORKFORCE", "team_composition", "5 Swarms (Executive, Coding, Content, Automation, WebOps) totaling 20 specialized autonomous agents.")
        ]
        cur.executemany("INSERT INTO zoey_memory (category, key_name, content) VALUES (?, ?, ?)", memories)

    conn.commit()
    conn.close()
    print("Zoey database schema migrated successfully.")

if __name__ == '__main__':
    init_zoey_tables()
