# ZOEY AI — DATABASE SCHEMA & ENTITY MAPPING
**Database:** `autonomous-org-core/data/gomyweblab_state.db`  
**Storage Engine:** SQLite3  

---

## 1. Existing Tables (Preserved)

### `users`
- `id` (INTEGER PRIMARY KEY)
- `username` (TEXT)
- `email` (TEXT)
- `password_hash` (TEXT)
- `role` (TEXT)
- `created_at` (DATETIME)

### `swarms`
- `id` (TEXT PRIMARY KEY)
- `name` (TEXT)
- `description` (TEXT)

### `agents`
- `id` (TEXT PRIMARY KEY)
- `name` (TEXT)
- `swarm_id` (TEXT)
- `role` (TEXT)
- `tag` (TEXT)
- `status` (TEXT)
- `api_key` (TEXT)
- `email` (TEXT)
- `current_task_title` (TEXT)
- `task_progress_pct` (INTEGER)
- `task_time_spent` (TEXT)
- `task_est_remaining` (TEXT)

### `tasks` & `decisions_log`
- Task definitions, client project mapping, verification scores, and automated approvals.

### `financial_ledger`
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `transaction_ref` (TEXT)
- `deal_ref` (TEXT)
- `client_name` (TEXT)
- `project_title` (TEXT)
- `platform` (TEXT)
- `amount_usd` (REAL)
- `payment_status` (TEXT: `RELEASED_EARNED`, `ESCROW_LOCKED`)
- `released_at` (DATETIME)
- `created_at` (DATETIME)

---

## 2. Zoey AI Extended Tables (New Migrations)

### `zoey_incidents`
```sql
CREATE TABLE IF NOT EXISTS zoey_incidents (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    severity TEXT NOT NULL, -- P0, P1, P2, P3
    department TEXT NOT NULL,
    source TEXT NOT NULL,
    business_impact TEXT NOT NULL,
    responsible_manager TEXT,
    recommended_action TEXT,
    status TEXT DEFAULT 'OPEN', -- OPEN, ACKNOWLEDGED, RESOLVED
    acknowledged_at DATETIME,
    resolved_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### `zoey_approvals`
```sql
CREATE TABLE IF NOT EXISTS zoey_approvals (
    id TEXT PRIMARY KEY,
    requested_action TEXT NOT NULL,
    requesting_agent TEXT NOT NULL,
    business_reason TEXT NOT NULL,
    expected_result TEXT,
    risk_level TEXT NOT NULL, -- LOW, MEDIUM, HIGH, CRITICAL
    related_record TEXT,
    proposed_payload TEXT,
    status TEXT DEFAULT 'PENDING', -- PENDING, APPROVED, REJECTED
    reviewed_by TEXT,
    reviewed_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### `zoey_memory`
```sql
CREATE TABLE IF NOT EXISTS zoey_memory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL, -- POLICY, EMPLOYEE, PROJECT, DECISION, PREFERENCE
    key_name TEXT NOT NULL,
    content TEXT NOT NULL,
    confidence REAL DEFAULT 1.0,
    source TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### `zoey_daily_reports`
```sql
CREATE TABLE IF NOT EXISTS zoey_daily_reports (
    id TEXT PRIMARY KEY,
    report_date TEXT NOT NULL,
    timezone TEXT DEFAULT 'Asia/Kolkata',
    executive_overview TEXT,
    employee_summary TEXT,
    project_performance TEXT,
    department_performance TEXT,
    sales_report TEXT,
    marketing_report TEXT,
    finance_summary TEXT,
    critical_issues TEXT,
    tomorrow_priorities TEXT,
    raw_json TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### `zoey_telephony_logs`
```sql
CREATE TABLE IF NOT EXISTS zoey_telephony_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    incident_id TEXT,
    recipient_phone TEXT,
    channel TEXT, -- WHATSAPP, VOICE_CALL
    provider TEXT, -- TWILIO, WHATSAPP_API
    status TEXT, -- QUEUED, SENT, DELIVERED, ACKNOWLEDGED, FAILED
    dtmf_input TEXT,
    response_payload TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```
