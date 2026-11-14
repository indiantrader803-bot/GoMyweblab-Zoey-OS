import os
import json
import sqlite3
import urllib.request
import urllib.parse
from datetime import datetime

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

class FreelancerOfficialClient:
    """
    Freelancer.com REST API Client implementing the official documentation standard:
    https://developers.freelancer.com/docs/api-overview/making-a-request
    
    Header Format:
      Freelancer-OAuth-v1: <token>
    """
    
    LIVE_BASE_URL = "https://www.freelancer.com/api"
    SANDBOX_BASE_URL = "https://www.freelancer-sandbox.com/api"

    def __init__(self, use_sandbox=False):
        self.env = load_env()
        self.token = self.env.get("FREELANCER_OAUTH_TOKEN", "").strip()
        self.base_url = self.SANDBOX_BASE_URL if use_sandbox else self.LIVE_BASE_URL

    def get_headers(self):
        headers = {
            "User-Agent": "GomyweblabAutonomousDirector/2.0",
            "Content-Type": "application/json"
        }
        if self.token:
            # As documented: 'Freelancer-OAuth-v1' or 'freelancer-oauth-v1'
            headers["Freelancer-OAuth-v1"] = self.token
        return headers

    def get_self_profile(self):
        """Fetches the authenticated user profile (whoami / balances)."""
        url = f"{self.base_url}/users/0.1/self"
        req = urllib.request.Request(url, headers=self.get_headers())
        try:
            with urllib.request.urlopen(req) as resp:
                return {"status": "SUCCESS", "data": json.loads(resp.read().decode())}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def search_active_projects(self, query="Next.js WordPress Python Automation", limit=10):
        """
        Searches active client projects using standard query parameters:
        GET /projects/0.1/projects/active?query=...&project_statuses[]=active
        """
        params = urllib.parse.urlencode({
            "query": query,
            "project_statuses[]": "active",
            "limit": limit,
            "compact": "true"
        })
        url = f"{self.base_url}/projects/0.1/projects/active?{params}"
        req = urllib.request.Request(url, headers=self.get_headers())
        try:
            with urllib.request.urlopen(req) as resp:
                res = json.loads(resp.read().decode())
                return {"status": "SUCCESS", "projects": res.get("result", {}).get("projects", [])}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def place_bid(self, project_id, amount, period_days, proposal_description):
        """
        Places a bid on an active project:
        POST /projects/0.1/bids/
        Payload: { "project_id": 123, "bidder_id": <self_id>, "amount": 250, "period": 3, "description": "..." }
        """
        if not self.token:
            return {"status": "BLOCKED", "message": "Valid FREELANCER_OAUTH_TOKEN required in freelance_accounts.env to submit bids."}

        url = f"{self.base_url}/projects/0.1/bids/"
        payload = json.dumps({
            "project_id": int(project_id),
            "amount": float(amount),
            "period": int(period_days),
            "description": proposal_description
        }).encode("utf-8")

        req = urllib.request.Request(url, data=payload, headers=self.get_headers(), method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                return {"status": "SUCCESS", "result": json.loads(resp.read().decode())}
        except urllib.error.HTTPError as he:
            err_body = he.read().decode()
            return {"status": "HTTP_ERROR", "code": he.code, "details": err_body}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def get_thread_messages(self, thread_id):
        """Fetches client conversation thread messages."""
        url = f"{self.base_url}/messages/0.1/threads/{thread_id}/messages"
        req = urllib.request.Request(url, headers=self.get_headers())
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def send_thread_reply(self, thread_id, message_text):
        """Autonomous Agent replies directly to client on Freelancer.com."""
        url = f"{self.base_url}/messages/0.1/threads/{thread_id}/messages"
        payload = json.dumps({"message": message_text}).encode("utf-8")
        req = urllib.request.Request(url, data=payload, headers=self.get_headers(), method="POST")
        try:
            with urllib.request.urlopen(req) as resp:
                return json.loads(resp.read().decode())
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

if __name__ == '__main__':
    client = FreelancerOfficialClient()
    print("Freelancer Client initialized.")
    search_res = client.search_active_projects(query="Full Stack WordPress AI", limit=2)
    print("Search Result:", search_res["status"], f"({len(search_res.get('projects', []))} projects found)")
