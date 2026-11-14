"""
Gomyweblab Autonomous Enterprise — Razorpay Payouts & Settlement Bridge
Enables automatic transfer of earned freelance & trading profits to your verified bank account / UPI via RazorpayX.
"""

import os
import json
import sqlite3
import datetime

try:
    import razorpay
except ImportError:
    razorpay = None

class RazorpayPayoutEngine:
    def __init__(self, key_id=None, key_secret=None, account_number=None, upi_id=None, recipient_name="Arnab Laha"):
        self.key_id = key_id or os.getenv("RAZORPAY_KEY_ID", "")
        self.key_secret = key_secret or os.getenv("RAZORPAY_KEY_SECRET", "")
        self.account_number = account_number or os.getenv("RAZORPAYX_ACCOUNT_NUMBER", "")
        self.upi_id = upi_id or os.getenv("RAZORPAY_UPI_ID", "8240438062@superyes")
        self.recipient_name = recipient_name
        self.client = None
        if razorpay and self.key_id and self.key_secret:
            try:
                self.client = razorpay.Client(auth=(self.key_id, self.key_secret))
            except Exception:
                self.client = None

    def get_status(self):
        """Returns payout gateway status and configuration readiness"""
        has_keys = bool(self.key_id and self.key_secret)
        return {
            "gateway": "RazorpayX Automated Payouts",
            "is_configured": has_keys,
            "recipient_name": self.recipient_name,
            "recipient_upi": self.upi_id,
            "key_id_masked": f"{self.key_id[:6]}...{self.key_id[-4:]}" if len(self.key_id) > 10 else "READY_FOR_SETTLEMENT",
            "account_number_masked": f"...{self.account_number[-4:]}" if len(self.account_number) >= 4 else "NOT_CONFIGURED",
            "currency": "INR",
            "payout_modes": ["IMPS", "NEFT", "RTGS", "UPI"],
            "settlement_schedule": "INSTANT_ON_RELEASE"
        }

    def create_payout_order(self, amount_inr, recipient_name=None, vpa_or_account=None, ifsc=None, purpose="Gomyweblab Autonomous Revenue Settlement"):
        """
        Executes a RazorpayX payout transfer to bank or UPI ID.
        If live API keys are not supplied yet, logs simulated settlement.
        """
        recipient_name = recipient_name or self.recipient_name
        vpa_or_account = vpa_or_account or self.upi_id
        ref_id = f"pout_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        if not self.client:
            return {
                "status": "QUEUED_PENDING_KEY",
                "reference_id": ref_id,
                "amount_inr": amount_inr,
                "recipient": recipient_name,
                "target": vpa_or_account,
                "message": "Payout transfer queued. Configure RAZORPAY_KEY_ID and RAZORPAY_KEY_SECRET to execute live wire transfer.",
                "timestamp": datetime.datetime.now().isoformat()
            }

        try:
            # 1. Contact / Fund Account Creation via RazorpayX
            payout_data = {
                "account_number": self.account_number,
                "amount": int(amount_inr * 100), # paise
                "currency": "INR",
                "mode": "UPI" if "@" in vpa_or_account else "IMPS",
                "purpose": "payout",
                "queue_if_low_balance": True,
                "reference_id": ref_id,
                "narration": purpose[:30]
            }
            # Execute through client request
            resp = self.client.post("/payouts", payout_data)
            return {"status": "SUCCESS", "payout": resp}
        except Exception as err:
            return {"status": "ERROR", "message": str(err), "reference_id": ref_id}

if __name__ == "__main__":
    engine = RazorpayPayoutEngine()
    print("Razorpay Gateway Status:", json.dumps(engine.get_status(), indent=2))
