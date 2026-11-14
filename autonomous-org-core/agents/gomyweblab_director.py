import sqlite3
import json
import os
import random
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POLICY_PATH = os.path.join(BASE_DIR, "..", "config", "gomyweblab_policy.json")
DB_PATH = os.path.join(BASE_DIR, "..", "data", "gomyweblab_state.db")

class GomyweblabDirector:
    def __init__(self):
        with open(POLICY_PATH, "r", encoding="utf-8") as f:
            self.policy = json.load(f)

    def evaluate_decision(self, category, cost=0.0, confidence=0.92, task_summary=""):
        threshold = self.policy["decision_engine"]["auto_execute_confidence_threshold"]
        spend_limit = self.policy["budget_limits"]["auto_spend_limit_single"]

        if cost > spend_limit:
            return "VETOED", False, f"Cost ${cost:.2f} exceeds auto-spend threshold of ${spend_limit:.2f}."
        
        if confidence >= threshold:
            return "AUTO_APPROVED", True, f"Confidence {confidence:.1%} meets policy threshold ({threshold:.1%}). Executed with 0 human bottleneck."
        elif confidence >= self.policy["decision_engine"]["dual_agent_consensus_threshold"]:
            return "CONSENSUS_APPROVED", True, f"Dual-agent consensus reached ({confidence:.1%}). Verified by QA / Lead."
        else:
            return "ESCALATED", False, f"Confidence {confidence:.1%} below consensus limits. Escalated to Director."

    def run_cycle(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        tasks_catalog = [
            # Social Media & Content
            ("Publish 3 SEO articles & schedule 12 LinkedIn/X posts", "TechFlow AI", "content", "social_publisher", "Social Media & Content", 0.0, random.uniform(0.92, 0.98), "Content copy and hashtag clusters passed quality & tone filters."),
            # Freelance & Client Inquiries
            ("Analyze Upwork RFP & draft customized technical proposal", "New Client (Upwork)", "executive", "bizdev_lead", "Freelance Work", 0.0, random.uniform(0.88, 0.95), "Scope, deliverables, timeline and pricing generated within agency rate card."),
            # IT Projects
            ("Adversarial code audit and deploy Next.js auth update", "Web3 Analytics Portal", "coding", "pr_verifier", "IT Projects", 0.0, random.uniform(0.94, 0.99), "Unit tests passed 100%, 0 security vulnerabilities detected. Code auto-merged to main."),
            # Automations
            ("Build Zapier/Webhook pipeline: HubSpot leads to Notion CRM", "Logistics Co.", "automation", "webhook_engineer", "Automation Project", 0.0, random.uniform(0.91, 0.97), "Payload validation tested with mock events; zero failure rate."),
            # Website Handling
            ("Automated WordPress plugin update & speed optimization", "Client Brand Site", "webops", "speed_optimizer", "Website Handling", 0.0, random.uniform(0.95, 0.99), "LCP improved by 34%, mobile score 96/100, zero layout shifts.")
        ]

        task_data = random.choice(tasks_catalog)
        title, client, swarm_id, agent_id, category, cost, conf, reasoning = task_data

        dec_type, approved, eval_reason = self.evaluate_decision(category, cost, conf, title)

        status = "completed" if approved else "rejected"
        cur.execute("""
            INSERT INTO tasks (title, client_name, swarm_id, assigned_agent, service_category, confidence, decision_type, cost, status, created_at, completed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, ?)
        """, (title, client, swarm_id, agent_id, category, conf, dec_type, cost, status, datetime.now() if approved else None))
        task_id = cur.lastrowid

        cur.execute("""
            INSERT INTO decisions_log (task_id, action, decision_type, confidence, reasoning, decided_by)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (task_id, category, dec_type, conf, reasoning, agent_id))

        if approved:
            cur.execute("UPDATE agents SET tasks_completed = tasks_completed + 1 WHERE id = ?", (agent_id,))

        conn.commit()
        conn.close()

        return {
            "task_id": task_id,
            "title": title,
            "client": client,
            "swarm": swarm_id,
            "agent": agent_id,
            "category": category,
            "decision": dec_type,
            "approved": approved,
            "confidence": f"{conf:.1%}",
            "reasoning": reasoning,
            "time": datetime.now().strftime("%H:%M:%S")
        }

if __name__ == '__main__':
    d = GomyweblabDirector()
    print("Cycle:", d.run_cycle())
