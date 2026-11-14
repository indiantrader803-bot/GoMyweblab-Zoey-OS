import sqlite3
import random
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "gomyweblab_state.db")

TASKS_BY_AGENT = {
    # TEAMS / EXECUTIVE
    "bizdev_lead": ("Scouting & Scoring Upwork RFPs", "Extracting high-ticket clients", 78, "24m", "6m"),
    "pm_director": ("Sprint & Milestone Allocation", "Syncing Gantt roadmap", 92, "45m", "4m"),
    "support_lead": ("Triage Inbound Client Chat Tickets", "Generating resolution draft", 65, "12m", "8m"),
    "finance_lead": ("Escrow Invoice Reconciliation", "Verifying milestone payments", 88, "35m", "5m"),
    
    # CODING
    "spec_writer": ("Drafting Next.js E-Commerce Spec", "Writing API contracts", 70, "28m", "14m"),
    "fullstack_dev": ("Building Stripe Webhook Handler", "Refactoring auth endpoints", 82, "50m", "10m"),
    "bug_hunter": ("Unit & Stress Testing Auth Token Cache", "Simulating 1,000 concurrency", 60, "15m", "10m"),
    "pr_verifier": ("Adversarial Security Audit on PR #104", "OWASP static analysis", 95, "40m", "2m"),

    # CONTENT
    "topic_researcher": ("Mining Viral Hooks on X & LinkedIn", "Extracting AI automation trends", 85, "32m", "6m"),
    "copy_artisan": ("Writing Technical Blog Post on AI Swarms", "Drafting sections 3 & 4", 75, "42m", "15m"),
    "social_publisher": ("Scheduling Omnichannel Posts", "Queueing media carousels", 90, "20m", "3m"),
    "seo_strategist": ("Backlink & Keyword Gap Clustering", "Generating sitemap matrix", 68, "25m", "12m"),

    # AUTOMATION
    "pipeline_architect": ("Designing Multi-Branch Zapier Flow", "Mapping Notion to HubSpot", 80, "38m", "8m"),
    "webhook_engineer": ("Deploying Cloudflare Worker API", "Testing payload encryption", 84, "22m", "5m"),
    "scraper_bot": ("Extracting 5k B2B Leads from Directories", "Deduplicating verified emails", 72, "48m", "18m"),
    "cron_supervisor": ("Self-Healing Heartbeat Watchdog", "Checking 14 active cron triggers", 99, "60m", "1m"),

    # WEBOPS
    "uptime_sentry": ("24/7 Global Ping & SSL Watch", "All endpoints 99.98% green", 96, "55m", "2m"),
    "security_guardian": ("WordPress Core Auto-Patching", "Verified zero-downtime backup", 88, "30m", "4m"),
    "speed_optimizer": ("Core Web Vitals & Image Compression", "LCP reduced from 3.2s to 1.1s", 91, "40m", "5m"),
    "backup_vault": ("Syncing Hourly Database Snapshots", "Uploading encrypted dump to S3", 100, "18m", "Done")
}

def seed_agent_live_tasks():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for agent_id, data in TASKS_BY_AGENT.items():
        title, subtask, pct, spent, rem = data
        cur.execute("""
            UPDATE agents 
            SET current_task_title = ?,
                active_subtask = ?,
                task_progress_pct = ?,
                task_time_spent = ?,
                task_est_remaining = ?
            WHERE id = ?
        """, (title, subtask, pct, spent, rem, agent_id))

    conn.commit()
    conn.close()
    print("Agent live task progress seeded successfully.")

if __name__ == '__main__':
    seed_agent_live_tasks()
