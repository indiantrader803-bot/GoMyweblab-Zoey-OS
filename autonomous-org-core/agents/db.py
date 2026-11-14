import sqlite3
import json
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "org_state.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Tasks Backlog
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        assigned_agent TEXT NOT NULL,
        priority TEXT DEFAULT 'medium',
        status TEXT DEFAULT 'pending', -- pending, in_progress, completed, rejected
        cost REAL DEFAULT 0.0,
        confidence REAL DEFAULT 0.95,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP
    )
    """)

    # Autonomous Decisions Ledger
    cur.execute("""
    CREATE TABLE IF NOT EXISTS decisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        action TEXT NOT NULL,
        decision_type TEXT NOT NULL, -- AUTO_APPROVED, CONSENSUS_APPROVED, VETOED, ESCALATED
        confidence REAL NOT NULL,
        reasoning TEXT,
        decided_by TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(task_id) REFERENCES tasks(id)
    )
    """)

    # Agent Roster / Status
    cur.execute("""
    CREATE TABLE IF NOT EXISTS agents (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        swarm TEXT NOT NULL,
        role TEXT NOT NULL,
        status TEXT DEFAULT 'online', -- online, busy, idle
        tasks_completed INTEGER DEFAULT 0,
        last_heartbeat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Seed Agents if empty
    cur.execute("SELECT COUNT(*) FROM agents")
    if cur.fetchone()[0] == 0:
        agents = [
            ('eng_lead', 'Engineering Lead', 'executive', 'Architecture & Sprint Manager'),
            ('marketing_director', 'Growth Director', 'executive', 'Omnichannel Strategy'),
            ('support_specialist', 'Support Sentinel', 'executive', 'Customer Success & Triage'),
            ('sales_lead', 'Outreach Pioneer', 'executive', 'B2B Lead Qualification'),
            ('spec_writer', 'Spec Architect', 'coding', 'Requirements to Technical Specs'),
            ('bug_reproducer', 'Bug Hunter', 'coding', 'Automated Repro & Isolation'),
            ('pr_producer', 'Code Synthesizer', 'coding', 'Feature & Patch Implementation'),
            ('pr_verifier', 'Adversarial Verifier', 'coding', 'Code Review, Security & Merges'),
            ('x_researcher', 'Market Scout', 'content', 'Viral Trend Mining & Keywords'),
            ('draft_generator', 'Content Artisan', 'content', 'Long-form & Thread Copywriting'),
            ('publisher', 'Distribution Node', 'content', 'Automated Syndication'),
            ('seo_optimizer', 'Search Authority', 'content', 'Programmatic SEO & Backlinks'),
            ('market_data', 'Telemetry Aggregator', 'trading', 'Orderbook & Feed Ingestion'),
            ('strategy_bot', 'Alpha Modeler', 'trading', 'Backtest & Factor Testing'),
            ('risk_officer', 'Veto Safeguard', 'trading', 'Position Sizing & Hard Drawdown Limits'),
            ('execution_engine', 'Order Router', 'trading', 'Slippage-minimized Execution'),
            ('coordinator', 'Firstmate Orchestrator', 'operations', 'Goal Decomposition & Event Bus'),
            ('memory_indexer', 'Corporate Memory', 'operations', 'SQLite & Vector Knowledge Store')
        ]
        cur.executemany("INSERT INTO agents (id, name, swarm, role) VALUES (?, ?, ?, ?)", agents)

    # Seed Sample Initial Tasks if empty
    cur.execute("SELECT COUNT(*) FROM tasks")
    if cur.fetchone()[0] == 0:
        sample_tasks = [
            ('Synthesize User Auth & RBAC Microservice', 'coding', 'pr_producer', 'high', 'completed', 0.0, 0.96),
            ('Analyze Competitor Backlink Opportunities', 'content', 'seo_optimizer', 'medium', 'completed', 0.0, 0.92),
            ('Scan Volatility Spreads on ETH/USDT Perp', 'trading', 'market_data', 'high', 'completed', 0.0, 0.98),
            ('Triage Inbound Support Tickets from Portal', 'executive', 'support_specialist', 'low', 'completed', 0.0, 0.95),
            ('Review Pull Request #48: Performance Optimization', 'coding', 'pr_verifier', 'high', 'in_progress', 0.0, 0.94)
        ]
        cur.executemany("INSERT INTO tasks (title, category, assigned_agent, priority, status, cost, confidence) VALUES (?, ?, ?, ?, ?, ?, ?)", sample_tasks)

    conn.commit()
    conn.close()
    print("Autonomous Org Database initialized at:", DB_PATH)

if __name__ == '__main__':
    init_db()
