"""
Actionsflow & Agent Automation Orchestration Bridge
Runs open-source n8n alternative Actionsflow jobs, triggers agent cycles,
and builds active workflow execution trees.
"""

import os
import subprocess
import json

WORKFLOW_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "actionsflow-workflows"))

def get_actionsflow_status():
    built_file = os.path.join(WORKFLOW_DIR, "dist", "workflows", "0-agent_sync-poll.yml")
    return {
        "engine": "Actionsflow (Open Source Zapier / n8n alternative)",
        "version": "1.12.1",
        "workflows_directory": os.path.join(WORKFLOW_DIR, "workflows"),
        "active_workflow": "agent_sync.yml",
        "compiled": os.path.exists(built_file),
        "trigger": "poll @ http://127.0.0.1:8088/api/status (every 15m)",
        "action": "GET http://127.0.0.1:8088/api/trigger-cycle",
        "status": "READY_AND_COMPILED"
    }

def run_actionsflow_build():
    try:
        proc = subprocess.run(
            ["actionsflow", "build"],
            cwd=WORKFLOW_DIR,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        return {
            "success": proc.returncode == 0,
            "stdout": proc.stdout.strip(),
            "stderr": proc.stderr.strip()
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    print(json.dumps(get_actionsflow_status(), indent=2))
