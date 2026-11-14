import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "data", "freelance_pipeline.db")

def init_freelance_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # Client Projects Lifecycle Table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS freelance_deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deal_ref TEXT UNIQUE,
        platform TEXT NOT NULL, -- Upwork, Fiverr, Freelancer, Direct
        client_name TEXT NOT NULL,
        client_country TEXT,
        project_title TEXT NOT NULL,
        project_description TEXT,
        client_budget REAL,
        market_benchmark_rate REAL,
        negotiated_budget REAL,
        current_stage TEXT NOT NULL,
        -- Stages: SCOUTED -> PROPOSAL_SENT -> IN_NEGOTIATION -> CONTRACT_AWARDED -> BUILDING -> DEMO_DEPLOYED -> FEEDBACK_REFINEMENT -> FINAL_HANDOVER -> PAID
        demo_url TEXT,
        client_feedback TEXT,
        handover_repo TEXT,
        confidence_score REAL DEFAULT 0.95,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Autonomous Message History with Client
    cur.execute("""
    CREATE TABLE IF NOT EXISTS client_conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deal_ref TEXT NOT NULL,
        sender TEXT NOT NULL, -- 'CLIENT' or 'AGENT:<AgentName>'
        message_text TEXT NOT NULL,
        intent TEXT, -- 'INQUIRY', 'COUNTER_OFFER', 'FEEDBACK', 'APPROVAL'
        decision_applied TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(deal_ref) REFERENCES freelance_deals(deal_ref)
    )
    """)

    # Seed with active lifecycle examples
    cur.execute("SELECT COUNT(*) FROM freelance_deals")
    if cur.fetchone()[0] == 0:
        deals = [
            ("DEAL-901", "Upwork", "David Sterling", "United States", "Full-Stack AI SaaS Dashboard with Stripe", 
             "Need a Next.js 14 dashboard integrated with OpenAI API and Stripe subscription checkout.", 
             1500.0, 2400.0, 2200.0, "DEMO_DEPLOYED", "https://demo-saas-david.gomyweblab.live", 
             "Looks incredible! Can you adjust the header color to navy blue and add CSV exports?", 
             "https://github.com/gomyweblab-delivery/david-saas-prod", 0.96),

            ("DEAL-902", "Fiverr Pro", "Elena Rostova", "Germany", "WordPress Speed Optimization & Security Hardening", 
             "E-commerce store loading in 7.4 seconds, need Core Web Vitals under 1.8s and malware cleanup.", 
             400.0, 650.0, 600.0, "FINAL_HANDOVER", "https://staging-speed.gomyweblab.live", 
             "Mobile score is now 98/100, approved for live server deployment!", 
             "https://gomyweblab-delivery/elena-wp-backup.zip", 0.99),

            ("DEAL-903", "Upwork", "Liam O'Connor", "United Kingdom", "Automated Make/Zapier CRM Sync Pipeline", 
             "Looking for an automation expert to route Facebook leads into HubSpot and trigger WhatsApp follow-ups.", 
             800.0, 1400.0, 1250.0, "IN_NEGOTIATION", None, 
             "Can we do $1,100 if we commit to milestone 2 next week?", None, 0.92),

            ("DEAL-904", "Direct RFP", "Kenji Sato", "Japan", "Custom Python Scraping & Lead Enrichment Bot", 
             "Extract 50k B2B verified emails from global logistics directories.", 
             900.0, 1600.0, 1500.0, "BUILDING", "https://demo-scraper.gomyweblab.live", 
             None, None, 0.95),

            ("DEAL-905", "Freelancer", "Sarah Jenkins", "Canada", "High-Converting SEO Landing Page for FinTech App", 
             "Modern UI design and copywriting in Tailwind CSS with micro-animations.", 
             500.0, 950.0, 900.0, "PROPOSAL_SENT", None, 
             None, None, 0.94)
        ]
        cur.executemany("""
            INSERT INTO freelance_deals (deal_ref, platform, client_name, client_country, project_title, project_description,
                                        client_budget, market_benchmark_rate, negotiated_budget, current_stage, demo_url,
                                        client_feedback, handover_repo, confidence_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, deals)

        # Seed conversations
        convs = [
            ("DEAL-901", "AGENT:Proposal Closer", "Hi David, Gomyweblab reviewed your Next.js + Stripe architecture requirements. Based on production security standards and webhook verification, our benchmark execution cost is $2,400. We can deliver your staging MVP in 48 hours for $2,200. Review our proposal.", "PROPOSAL", "AUTO_SENT"),
            ("DEAL-901", "CLIENT", "Sounds fair! Can you show me a working staging prototype before final milestone escrow?", "APPROVAL", "ACCEPTED"),
            ("DEAL-901", "AGENT:Demo Deployer", "David, your live interactive staging environment is deployed at https://demo-saas-david.gomyweblab.live with test Stripe checkout enabled. Please review.", "DEMO", "AUTO_DEPLOYED"),
            ("DEAL-901", "CLIENT", "Looks incredible! Can you adjust the header color to navy blue and add CSV exports?", "FEEDBACK", "QUEUED_REFINEMENT"),
            ("DEAL-903", "AGENT:Rate Negotiator", "Hello Liam, standard enterprise Zapier & HubSpot webhook architectures run $1,400 with retries and failure alerts. We offer a milestone tier at $1,250.", "NEGOTIATION", "AUTO_COUNTERED"),
            ("DEAL-903", "CLIENT", "Can we do $1,100 if we commit to milestone 2 next week?", "COUNTER_OFFER", "PENDING_CONSENSUS")
        ]
        cur.executemany("""
            INSERT INTO client_conversations (deal_ref, sender, message_text, intent, decision_applied)
            VALUES (?, ?, ?, ?, ?)
        """, convs)

    conn.commit()
    conn.close()
    print("Freelance Pipeline DB initialized.")

if __name__ == '__main__':
    init_freelance_db()
