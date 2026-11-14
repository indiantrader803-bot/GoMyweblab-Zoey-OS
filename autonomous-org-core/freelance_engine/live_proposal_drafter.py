"""
FREELANCER.COM LIVE PROPOSAL & CONTEST DRAFTER ENGINE
Scouts active real-time projects and contests on Freelancer.com,
crafts winning proposals adhering strictly to Freelancer.com guidelines:
- https://www.freelancer.com/articles/freelancer-insights/writing-a-winning-bid
Stores drafted proposals ready for 1-click submission by Director Arnab.
"""

import os
import sys
import json
import sqlite3
import urllib.request
import urllib.parse
from datetime import datetime

CORE_DIR = os.path.dirname(os.path.abspath(__file__))
CONNECTORS_DIR = os.path.join(CORE_DIR, "..", "connectors")
DATA_DIR = os.path.join(CORE_DIR, "..", "data")
FREELANCE_DB = os.path.join(DATA_DIR, "freelance_pipeline.db")
GOMY_DB = os.path.join(DATA_DIR, "gomyweblab_state.db")

sys.path.append(CONNECTORS_DIR)
from freelancer_official import FreelancerOfficialClient

class LiveProposalDrafter:
    def __init__(self):
        self.client = FreelancerOfficialClient()

    def generate_winning_proposal(self, title, desc, budget_min, budget_max, currency="USD"):
        """
        Drafts a winning bid adhering to Freelancer.com guidelines:
        1. Professional greeting & direct statement of understanding.
        2. Clear breakdown of technical solution & milestones.
        3. Benchmark pricing and timeline.
        4. Clear call to action (invitation to discuss via chat).
        """
        mid_budget = (budget_min + budget_max) / 2 if budget_max > budget_min else budget_min
        if mid_budget == 0:
            mid_budget = 50.0

        bid_amount = round(mid_budget * 0.95, 2)  # slightly competitive
        period_days = 3 if bid_amount < 150 else 5

        proposal_text = (
            f"Hi there,\n\n"
            f"I reviewed your project requirement: \"{title}\". "
            f"Our team specializes in full-stack Python engineering, workflow automation, and custom web applications, "
            f"delivering clean, production-grade solutions that strictly match your functional criteria.\n\n"
            f"### Proposed Execution Strategy & Milestones:\n"
            f"1. **Phase 1: Architecture & Data Model:** Immediate setup of the core logic, schema, and API interface within 24 hours.\n"
            f"2. **Phase 2: Core Development & Automation:** Full implementation with unit tests to ensure 100% bug-free behavior.\n"
            f"3. **Phase 3: Client Review & Staging Preview:** We provide a live staging demo URL so you can inspect and test the deliverable firsthand.\n"
            f"4. **Phase 4: Deployment & Final Handover:** Clean codebase delivery with clear setup documentation and deployment assistance.\n\n"
            f"### Commercials:\n"
            f"- **Proposed Bid:** ${bid_amount:,.2f} {currency}\n"
            f"- **Estimated Delivery:** {period_days} Days\n\n"
            f"We are ready to start immediately. Feel free to open a chat so we can discuss the specific details and launch the first milestone!\n\n"
            f"Best regards,\n"
            f"Arnab & The Autonomous Engineering Team"
        )

        return {
            "bid_amount": bid_amount,
            "period_days": period_days,
            "proposal_text": proposal_text
        }

    def scout_and_draft_live_bids(self, limit=5):
        """Scouts live projects from Freelancer.com API and stores drafted proposals."""
        res = self.client.search_active_projects(query="Python Automation Website", limit=limit)
        projects = res.get("projects", [])

        conn = sqlite3.connect(FREELANCE_DB)
        cur = conn.cursor()

        drafts = []
        for p in projects:
            proj_id = p.get("id")
            title = p.get("title")
            budget_info = p.get("budget", {})
            b_min = float(budget_info.get("minimum", 0) or 0)
            b_max = float(budget_info.get("maximum", 0) or 0)
            currency_code = budget_info.get("currency", {}).get("code", "USD") if isinstance(budget_info.get("currency"), dict) else "USD"

            seo_url = p.get("seo_url") or f"projects/{proj_id}"
            direct_link = f"https://www.freelancer.com/projects/{seo_url}"

            draft = self.generate_winning_proposal(title, p.get("preview_description", ""), b_min, b_max, currency_code)

            deal_ref = f"FL-{proj_id}"
            cur.execute("SELECT id FROM freelance_deals WHERE deal_ref = ?", (deal_ref,))
            existing = cur.fetchone()

            if not existing:
                cur.execute("""
                    INSERT INTO freelance_deals (
                        deal_ref, platform, client_name, client_country, project_title,
                        client_budget, market_benchmark_rate, negotiated_budget,
                        current_stage, confidence_score, demo_url
                    ) VALUES (?, 'Freelancer.com', 'Verified Client', 'Global', ?, ?, ?, ?, 'DRAFTED_WINNING_BID', 0.98, ?)
                """, (deal_ref, title, b_min, b_max, draft["bid_amount"], direct_link))

                cur.execute("""
                    INSERT INTO client_conversations (deal_ref, sender, message_text, intent, decision_applied)
                    VALUES (?, 'ZOEY:Proposal Bot', ?, 'PROPOSAL_DRAFT', 'READY_TO_SUBMIT')
                """, (deal_ref, draft["proposal_text"]))

            drafts.append({
                "project_id": proj_id,
                "title": title,
                "direct_link": direct_link,
                "bid_amount": draft["bid_amount"],
                "period_days": draft["period_days"],
                "proposal_text": draft["proposal_text"]
            })

        conn.commit()
        conn.close()
        return drafts

if __name__ == '__main__':
    drafter = LiveProposalDrafter()
    bids = drafter.scout_and_draft_live_bids(limit=3)
    print(f"Generated {len(bids)} live winning bids ready for 1-click submission.")
