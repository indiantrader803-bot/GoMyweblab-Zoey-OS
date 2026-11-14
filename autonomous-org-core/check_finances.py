import sqlite3

conn = sqlite3.connect('autonomous-org-core/data/gomyweblab_state.db')
cur = conn.cursor()
cols = [r[1] for r in cur.execute("PRAGMA table_info(financial_ledger)").fetchall()]
print("financial_ledger columns:", cols)
rows = cur.execute("SELECT * FROM financial_ledger").fetchall()
for r in rows:
    print(r)

cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'RELEASED_EARNED'")
earned = cur.fetchone()[0]
cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'ESCROW_LOCKED'")
escrow = cur.fetchone()[0]
print(f"Total Earned: ${earned:.2f}, In Escrow: ${escrow:.2f}")

conn.close()
