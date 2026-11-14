"""
EXPERIENTIAL LABS AI CLIENT CONNECTOR
Provides OpenAI-compatible interface to Experiential Labs AI API:
Base URL: https://api.experientiallabs.ai/v1
Supported Models: aion-2.0, claude-opus-latest, gemini-3-flash, deepseek-r1, gpt-4o, etc.
"""

import os
import json
import urllib.request
import urllib.error

EXPERIENTIAL_API_KEY = os.getenv("EXPERIENTIAL_API_KEY", "xpl_ecc6a44d010d576a8e429d3e42743fd3f8bc95ab")
EXPERIENTIAL_BASE_URL = "https://api.experientiallabs.ai/v1"

class ExperientialLabsClient:
    def __init__(self, api_key=None, default_model="aion-2.0"):
        self.api_key = api_key or EXPERIENTIAL_API_KEY
        self.default_model = default_model

    def list_models(self):
        """Fetches list of available models from Experiential Labs."""
        url = f"{EXPERIENTIAL_BASE_URL}/models"
        req = urllib.request.Request(
            url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": "GomyweblabZoey/2.0"
            }
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                return {"status": "SUCCESS", "models": [m["id"] for m in data.get("data", [])]}
        except urllib.error.HTTPError as he:
            return {"status": "HTTP_ERROR", "code": he.code, "error": he.read().decode()}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def complete_chat(self, messages, model=None, max_tokens=500, temperature=0.7):
        """Sends chat completion request to Experiential Labs."""
        url = f"{EXPERIENTIAL_BASE_URL}/chat/completions"
        target_model = model or self.default_model

        body = {
            "model": target_model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "GomyweblabZoey/2.0"
            },
            method="POST"
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choice = data.get("choices", [{}])[0].get("message", {})
                return {
                    "status": "SUCCESS",
                    "model": data.get("model", target_model),
                    "content": choice.get("content", ""),
                    "raw": data
                }
        except urllib.error.HTTPError as he:
            err_msg = he.read().decode("utf-8")
            return {"status": "HTTP_ERROR", "code": he.code, "error": err_msg}
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

if __name__ == '__main__':
    client = ExperientialLabsClient()
    models_res = client.list_models()
    print("Catalog Status:", models_res["status"], f"({len(models_res.get('models', []))} models)")
