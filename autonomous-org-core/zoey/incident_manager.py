"""
ZOEY AI INCIDENT MANAGEMENT SYSTEM
Deterministic rules and contextual severity classification (P0, P1, P2, P3)
"""

import os
import json
import sqlite3
import uuid
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "gomyweblab_state.db")

class IncidentManager:
    def __init__(self):
        pass

    def create_incident(self, title, description, severity, department, source, business_impact, responsible_manager, recommended_action):
        incident_id = f"INC-{datetime.now().strftime('%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO zoey_incidents 
            (id, title, description, severity, department, source, business_impact, responsible_manager, recommended_action, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'OPEN')
        """, (incident_id, title, description, severity.upper(), department, source, business_impact, responsible_manager, recommended_action))
        conn.commit()
        conn.close()

        # If P0, trigger telephony verification
        if severity.upper() == 'P0':
            from telephony_bridge import TelephonyBridge
            tb = TelephonyBridge()
            tb.trigger_p0_call(incident_id, title, department, business_impact, recommended_action)
            tb.send_whatsapp_alert(incident_id, severity, title, department, business_impact, recommended_action)

        return {"id": incident_id, "status": "OPEN", "severity": severity.upper()}

    def acknowledge_incident(self, incident_id):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            UPDATE zoey_incidents
            SET status = 'ACKNOWLEDGED', acknowledged_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (incident_id,))
        conn.commit()
        conn.close()
        return {"id": incident_id, "status": "ACKNOWLEDGED"}

    def resolve_incident(self, incident_id):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            UPDATE zoey_incidents
            SET status = 'RESOLVED', resolved_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (incident_id,))
        conn.commit()
        conn.close()
        return {"id": incident_id, "status": "RESOLVED"}

    def list_incidents(self, limit=20):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            SELECT id, title, description, severity, department, source, business_impact, responsible_manager, recommended_action, status, acknowledged_at, resolved_at, created_at
            FROM zoey_incidents
            ORDER BY created_at DESC LIMIT ?
        """, (limit,))
        rows = cur.fetchall()
        conn.close()

        return [{
            "id": r[0], "title": r[1], "description": r[2], "severity": r[3], "department": r[4],
            "source": r[5], "business_impact": r[6], "manager": r[7], "action": r[8],
            "status": r[9], "acknowledged_at": r[10], "resolved_at": r[11], "created_at": r[12]
        } for r in rows]

if __name__ == '__main__':
    im = IncidentManager()
    # Seed a sample baseline non-emergency incident if empty
    incidents = im.list_incidents()
    if not incidents:
        im.create_incident(
            "Delta Exchange India Tick Sync Reconnected",
            "WebSocket tick buffer experienced 1.2s reconnect jitter. Zero open orders affected.",
            "P3", "Trading & WebOps", "LiveTradingBridge",
            "Minor telemetry latency; circuit breaker verified intact.",
            "AI Technical Manager", "Continue automated socket health ping."
        )
    print("Incidents Total:", len(im.list_incidents()))
