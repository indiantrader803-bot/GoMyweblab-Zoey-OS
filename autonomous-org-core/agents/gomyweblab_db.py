import sqlite3
import json
import os
import random
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POLICY_PATH = os.path.join(BASE_DIR, "..", "config", "gomyweblab_policy.json")
DB_PATH = os.path.join(BASE_DIR, "..", "data", "gomyweblab_state.db")

def init_gomyweblab():
    with open(POLICY_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS swarms (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        job TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS agents (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        swarm_id TEXT NOT NULL,
        role TEXT NOT NULL,
        tag TEXT NOT NULL,
        status TEXT DEFAULT 'online',
        tasks_completed INTEGER DEFAULT 0,
        last_action TEXT,
        FOREIGN KEY(swarm_id) REFERENCES swarms(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        client_name TEXT DEFAULT 'Internal / Gomyweblab',
        swarm_id TEXT NOT NULL,
        assigned_agent TEXT NOT NULL,
        service_category TEXT NOT NULL,
        priority TEXT DEFAULT 'high',
        status TEXT DEFAULT 'completed', -- pending, in_progress, completed, vetoed
        confidence REAL DEFAULT 0.95,
        decision_type TEXT DEFAULT 'AUTO_APPROVED',
        cost REAL DEFAULT 0.0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS decisions_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        action TEXT NOT NULL,
        decision_type TEXT NOT NULL,
        confidence REAL NOT NULL,
        reasoning TEXT,
        decided_by TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Populate swarms and agents
    cur.execute("DELETE FROM swarms")
    cur.execute("DELETE FROM agents")

    for s_key, s_data in config.get("swarms", {}).items():
        cur.execute("INSERT INTO swarms (id, title, job) VALUES (?, ?, ?)", (s_key, s_data["title"], s_data["job"]))
        for ag in s_data.get("agents", []):
            cur.execute("""
                INSERT INTO agents (id, name, swarm_id, role, tag, status, tasks_completed, last_action)
                VALUES (?, ?, ?, ?, ?, 'online', ?, ?)
            """, (ag["id"], ag["name"], s_key, ag["role"], ag["tag"], random.randint(12, 85), ag["tag"]))

    # Seed initial real-world tasks for Gomyweblab
    cur.execute("SELECT COUNT(*) FROM tasks")
    if cur.fetchone()[0] == 0:
        sample_tasks = [
            ("Client Proposal: Draft $2,500 Full-Stack E-Commerce IT Proposal", "Acme Retailers", "executive", "bizdev_lead", "Freelance Work", 0.94, "AUTO_APPROVED", 0.0, "Auto-generated technical milestone breakdown and scope matrix."),
            ("Social Media: Schedule 5 Educational Carousels on AI Automation", "SaaS Client X", "content", "social_publisher", "Social Media Management", 0.98, "AUTO_APPROVED", 0.0, "Omnichannel queue synchronized for LinkedIn and X."),
            ("Website Maintenance: WordPress Core & Plugin Patching + Uptime Verification", "LawFirmOnline.com", "webops", "security_guardian", "Website Handling", 0.99, "AUTO_APPROVED", 0.0, "Zero-downtime staging backup verified before hot-patching."),
            ("Automation Pipeline: Sync Stripe Inbound Payments to Google Sheets & Slack", "FinTech Startup", "automation", "webhook_engineer", "Automation Project", 0.95, "AUTO_APPROVED", 0.0, "Webhook endpoint tested and error handling fallback enabled."),
            ("IT Project: Code Review & Security Audit for Next.js Client Dashboard", "HealthTech Partner", "coding", "pr_verifier", "IT Projects", 0.96, "AUTO_APPROVED", 0.0, "OWASP security pass completed with 0 vulnerabilities detected.")
        ]
        for t in sample_tasks:
            cur.execute("""
                INSERT INTO tasks (title, client_name, swarm_id, assigned_agent, service_category, confidence, decision_type, cost, status, created_at, completed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'completed', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """, (t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7]))
            task_id = cur.lastrowid
            cur.execute("""
                INSERT INTO decisions_log (task_id, action, decision_type, confidence, reasoning, decided_by)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (task_id, t[4], t[6], t[5], t[8], t[3]))

    conn.commit()
    conn.close()
    print("Gomyweblab Database initialized successfully!")

if __name__ == '__main__':
    init_gomyweblab()
