# ZOEY AI — SYSTEM ARCHITECTURE
**Role:** AI Chief Operating Officer (COO) & Business Operating System  
**Version:** 1.0.0-ENTERPRISE  
**Base Platform:** GoMyWebLab Autonomous OS & Multi-Agent Matrix

---

## 1. High-Level Architectural Diagram

```
+-----------------------------------------------------------------------------------+
|                            DIRECTOR / OWNER INTERACTION                            |
|             Web Command Center  |  WhatsApp Bot Alerts  |  Twilio Voice Emergency  |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                               ZOEY AI ORCHESTRATOR                                |
|  - Natural Language Intent Parser    - Task Planning & Work Decomposition         |
|  - Multi-Agent Delegation Engine     - Context & Execution History Manager        |
|  - Deterministic Verification Gate   - Approval & Escalation Controller           |
+-----------------------------------------------------------------------------------+
                                          |
            +-----------------------------+-----------------------------+
            |                                                           |
            v                                                           v
+-----------------------+                                   +-----------------------+
|  ZOEY 9 SPECIALIST    |                                   |  ZOEY CORE SERVICES   |
|     AI MANAGERS       |                                   |                       |
| 1. Zoey COO           |                                   | - Daily Reporting     |
| 2. AI HR Manager      |                                   |   (6:00 PM IST)       |
| 3. AI Project Manager |                                   | - Incident Engine     |
| 4. AI Marketing Mgr   |                                   |   (P0/P1/P2/P3)       |
| 5. AI Sales Manager   |                                   | - Approval Center     |
| 6. AI Finance Analyst |                                   | - Persistent Memory   |
| 7. AI Research Analyst|                                   | - WhatsApp API        |
| 8. AI Technical Mgr   |                                   | - Phone Voice Alert   |
| 9. AI Executive Assist|                                   | - n8n Automations     |
+-----------------------+                                   +-----------------------+
            |                                                           |
            +-----------------------------+-----------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                         COMPANY APPLICATION CORE & DATA                           |
|  - 20 Live Execution Agents (Coding, Content, Automation, WebOps, Executive)      |
|  - SQLite Database (State, Tasks, Ledgers, Heartbeats, Decisions, Incidents)     |
|  - Live Trading Bridge (Delta India, CoinSwitch, Coinbase)                        |
|  - Freelance Bidding & Invoicing Engine (Freelancer API, RazorpayX UPI Settlement)|
+-----------------------------------------------------------------------------------+
```

---

## 2. Component Specifications

### 2.1 Zoey Orchestrator (`zoey_orchestrator.py`)
- Coordinates multi-step operations using deterministic intent routing and local AI generation.
- Enforces strict verification: never marks a task completed unless verified through return codes or database records.
- Implements 4 permission levels: `READ`, `PROPOSE`, `ROUTINE EXECUTION`, and `APPROVAL REQUIRED`.

### 2.2 9 Specialist AI Employees
1. **Zoey COO:** Overall operational health, bottleneck identification, agent orchestration.
2. **AI HR Manager:** Workload allocation, agent uptime, shift scheduling.
3. **AI Project Manager:** Milestones, task completion deadlines, blocker remediation.
4. **AI Marketing Manager:** Content calendars, syndication campaigns, SEO reviews.
5. **AI Sales Manager:** Lead tracking, proposal negotiation rates, client follow-up.
6. **AI Finance Analyst:** Cash flow analysis, ledger reconciliation, margin protection.
7. **AI Research Analyst:** Market intelligence, competitor benchmarking, trend analysis.
8. **AI Technical Manager:** Uptime sentry, PR verifications, code quality audits.
9. **AI Executive Assistant:** Agenda coordination, daily briefings, priority checklists.

### 2.3 Emergency Alerting Engine (WhatsApp & Telephony)
- **WhatsApp Webhook:** Delivers P0/P1 incident notifications and 6:00 PM IST executive summaries.
- **Twilio Voice Call:** Initiated exclusively for verified P0 critical incidents with automated voice briefing and DTMF acknowledgment (Press 1 to acknowledge).
