with open('autonomous-org-core/agents/server.py', 'r', encoding='utf-8') as f:
    server_code = f.read()

target_block = '''        # 5. Open Source Alternatives Catalog'''

new_endpoint = '''        # 4b. Real Financial Ledger & Earned Revenue Endpoint
        elif parsed.path == "/api/financial-ledger":
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'RELEASED_EARNED'")
            total_earned = cur.fetchone()[0]
            cur.execute("SELECT COALESCE(SUM(amount_usd), 0.0) FROM financial_ledger WHERE payment_status = 'ESCROW_LOCKED'")
            in_escrow = cur.fetchone()[0]
            cur.execute("""
                SELECT id, transaction_ref, deal_ref, client_name, project_title, platform, amount_usd, payment_status, released_at, created_at 
                FROM financial_ledger 
                ORDER BY id DESC
            """)
            ledger_items = [{
                "id": r[0], "ref": r[1], "deal_ref": r[2], "client": r[3], "title": r[4], 
                "platform": r[5], "amount": r[6], "status": r[7], "released_at": r[8], "date": r[9]
            } for r in cur.fetchall()]
            conn.close()

            self.send_json({
                "status": "SUCCESS",
                "total_earned_usd": total_earned,
                "in_escrow_usd": in_escrow,
                "currency": "USD",
                "upi_settlement": "8240438062@superyes",
                "director": "Arnab",
                "ledger": ledger_items
            })
            return

        # 5. Open Source Alternatives Catalog'''

if target_block in server_code and '/api/financial-ledger' not in server_code:
    server_code = server_code.replace(target_block, new_endpoint)
    with open('autonomous-org-core/agents/server.py', 'w', encoding='utf-8') as f:
        f.write(server_code)
    print("Added /api/financial-ledger endpoint to server.py")
else:
    print("Target block not found or endpoint already present.")
