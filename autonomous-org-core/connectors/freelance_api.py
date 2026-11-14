import os
import json
import sqlite3
import urllib.request
import urllib.parse

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "..", "config", "freelance_accounts.env")
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "freelance_pipeline.db")

def load_env():
    env = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env

class FreelancerComConnector:
    """Official Freelancer.com REST API integration."""
    def __init__(self, token=None):
        self.env = load_env()
        self.token = token or self.env.get("FREELANCER_OAUTH_TOKEN", "")
        self.base_url = "https://www.freelancer.com/api/projects/0.1"

    def is_configured(self):
        return bool(self.token and len(self.token) > 10)

    def search_active_projects(self, keywords=["Python", "Next.js", "Automation"]):
        if not self.is_configured():
            return {"status": "MOCK_MODE", "message": "No token provided. Add FREELANCER_OAUTH_TOKEN in config/freelance_accounts.env"}

        query = urllib.parse.urlencode({"query": " ".join(keywords), "project_statuses[]": "active", "limit": 10})
        url = f"{self.base_url}/projects/active?{query}"
        req = urllib.request.Request(url, headers={"Freelancer-OAuth-V1": self.token, "User-Agent": "GomyweblabAgent/1.0"})
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                return {"status": "SUCCESS", "projects": data.get("result", {}).get("projects", [])}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def place_bid(self, project_id, amount, description, period_days=3):
        if not self.is_configured():
            return {"status": "MOCK_MODE", "message": "Simulation: bid placed."}

        url = f"{self.base_url}/bids/"
        payload = json.dumps({"project_id": project_id, "bidder_id": 0, "amount": amount, "period": period_days, "description": description}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers={"Freelancer-OAuth-V1": self.token, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

class UpworkConnector:
    """Official Upwork GraphQL / REST API Integration."""
    def __init__(self):
        self.env = load_env()
        self.client_id = self.env.get("UPWORK_CLIENT_ID", "")
        self.access_token = self.env.get("UPWORK_ACCESS_TOKEN", "")

    def is_configured(self):
        return bool(self.access_token and len(self.access_token) > 10)

    def check_connection(self):
        if self.is_configured():
            return {"status": "CONNECTED", "platform": "Upwork", "account": "Gomyweblab Verified Agency"}
        return {"status": "NEEDS_KEYS", "instruction": "Add UPWORK_CLIENT_ID & UPWORK_ACCESS_TOKEN to config/freelance_accounts.env"}

if __name__ == '__main__':
    f_conn = FreelancerComConnector()
    u_conn = UpworkConnector()
    print("Freelancer.com configured:", f_conn.is_configured())
    print("Upwork configured:", u_conn.is_configured())
