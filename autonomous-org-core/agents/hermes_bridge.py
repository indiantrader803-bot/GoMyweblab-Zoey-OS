"""
Hermes Agent Enterprise Bridge for Gomyweblab Autonomous Organization
Allows any agent, workflow (n8n, actionsflow, zero), or dashboard endpoint
to run Hermes Agent with specific queries, toolsets, and reasoning effort.
"""

import os
import sys
import subprocess
import json

HERMES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "hermes-agent"))
CLI_PATH = os.path.join(HERMES_DIR, "cli.py")

def get_hermes_status():
    installed = os.path.exists(CLI_PATH)
    return {
        "installed": installed,
        "repo_path": HERMES_DIR,
        "cli_path": CLI_PATH,
        "capabilities": [
            "interactive_sessions",
            "oneshot_execution",
            "skills_loading",
            "git_worktrees",
            "custom_providers"
        ]
    }

def run_hermes_task(query: str, oneshot: bool = True, model: str = None, toolsets: str = None):
    if not os.path.exists(CLI_PATH):
        return {"error": "Hermes Agent CLI not found at " + CLI_PATH}
        
    cmd = [sys.executable, CLI_PATH, f"--query={query}"]
    if oneshot:
        cmd.append("--oneshot=True")
    if model:
        cmd.append(f"--model={model}")
    if toolsets:
        cmd.append(f"--toolsets={toolsets}")
        
    try:
        proc = subprocess.run(cmd, cwd=HERMES_DIR, capture_output=True, text=True, timeout=60)
        return {
            "status": "success" if proc.returncode == 0 else "error",
            "exit_code": proc.returncode,
            "output": proc.stdout.strip(),
            "stderr": proc.stderr.strip()
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    status = get_hermes_status()
    print("Hermes Status:", json.dumps(status, indent=2))
