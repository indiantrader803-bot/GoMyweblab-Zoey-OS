"""
J.A.R.V.I.S. SmartMag Autonomous Programmatic SEO & First-Page Rank Engine
Monitors, audits, generates high-intent keywords, sitemap pings, and on-page schema
for all 4 primary digital assets:
1. https://thesmartmag.com/ (Main publication: AI, Tech, Web3, FinTech)
2. https://thesmartmag.com/store (AI Tools, Tech Gadgets & SaaS Hub)
3. https://thesmartmag.com/travel (AI Travel Concierge, Aviasales & Luxury Bookings)
4. https://trade.thesmartmag.com/ (Quant Neural Terminal, Prop Firm & MT5 Copy Trading)
"""

import os
import json
import sqlite3
import urllib.request
import re
from datetime import datetime

SMARTMAG_TARGETS = {
    "home": {
        "url": "https://thesmartmag.com/",
        "title": "TheSmartMag — AI, Technology, Finance & Markets",
        "primary_keywords": [
            "AI technology news 2026",
            "fintech market analysis",
            "autonomous AI agents guide",
            "smart tech trends"
        ],
        "target_audience": "Tech founders, developers, quantitative traders, AI innovators"
    },
    "store": {
        "url": "https://thesmartmag.com/store",
        "title": "TheSmartMag Store — Trending AI Tools, Tech & Premium Gear",
        "primary_keywords": [
            "best AI tools 2026",
            "buy AI developer gear",
            "trending AI software subscriptions",
            "smart office gadgets"
        ],
        "target_audience": "Software engineers, remote workers, AI creators"
    },
    "travel": {
        "url": "https://thesmartmag.com/travel",
        "title": "SmartMag Travel — AI Trip Planner, Cheap Flights & Luxury Deals",
        "primary_keywords": [
            "AI travel planner free",
            "cheap flight ticket finder 2026",
            "luxury hotel discounts AI",
            "personalized vacation itinerary builder"
        ],
        "target_audience": "Digital nomads, global travelers, holiday planners"
    },
    "trade": {
        "url": "https://trade.thesmartmag.com/",
        "title": "TheSmartMag Quant Terminal — Autonomous Prop Firm & Multi-Exchange AI",
        "primary_keywords": [
            "autonomous AI trading terminal",
            "prop firm copy trading bot",
            "MT5 algorithmic trade replication",
            "crypto perpetual futures AI signals"
        ],
        "target_audience": "Fund managers, algorithmic traders, prop firm challenge candidates"
    }
}

class JarvisSmartMagSEOEngine:
    def __init__(self, db_path=None):
        if not db_path:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(base_dir, "data", "smartmag_seo.db")
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS seo_audits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_key TEXT,
                url TEXT,
                status_code INTEGER,
                title TEXT,
                description_len INTEGER,
                h1_text TEXT,
                canonical TEXT,
                has_schema INTEGER,
                robots TEXT,
                health_score REAL,
                recommendations TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS keyword_clusters (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_key TEXT,
                keyword TEXT,
                search_intent TEXT,
                target_position TEXT,
                action_required TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def audit_target(self, key, target):
        url = target["url"]
        score = 100.0
        recs = []
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                status_code = resp.status
                html = resp.read().decode('utf-8', errors='ignore')
                
                # Check Title
                title_match = re.search(r'<title>(.*?)</title>', html, re.I | re.S)
                title = title_match.group(1).strip() if title_match else ""
                if not title:
                    score -= 20
                    recs.append("Missing <title> tag")
                elif len(title) > 70:
                    score -= 5
                    recs.append(f"Title is {len(title)} chars (recommended: 50-60 chars)")

                # Check Meta Description
                desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
                if not desc_match:
                    desc_match = re.search(r'<meta\s+content=["\'](.*?)["\']\s+name=["\']description["\']', html, re.I | re.S)
                desc = desc_match.group(1).strip() if desc_match else ""
                desc_len = len(desc)
                if not desc:
                    score -= 20
                    recs.append("Missing meta description")
                elif desc_len < 120 or desc_len > 165:
                    recs.append(f"Meta description length is {desc_len} chars (optimal: 140-160 chars)")

                # Check H1
                h1_matches = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)
                h1_text = re.sub(r'<[^>]+>', '', h1_matches[0]).strip() if h1_matches else ""
                if not h1_matches:
                    score -= 15
                    recs.append("Missing H1 heading on landing page")
                elif len(h1_matches) > 1:
                    score -= 5
                    recs.append(f"Multiple H1 tags detected ({len(h1_matches)}); consolidate to 1 main semantic H1")

                # Check Canonical
                canon_match = re.search(r'<link\s+rel=["\']canonical["\']\s+href=["\'](.*?)["\']', html, re.I | re.S)
                canonical = canon_match.group(1).strip() if canon_match else ""
                if not canonical:
                    score -= 10
                    recs.append("Add explicit self-referential rel=canonical tag")

                # Schema
                has_schema = 1 if 'application/ld+json' in html else 0
                if not has_schema:
                    score -= 15
                    recs.append("Missing structured Schema.org JSON-LD (Article/Product/SoftwareApplication)")

                # Robots
                robots_match = re.search(r'<meta\s+name=["\']robots["\']\s+content=["\'](.*?)["\']', html, re.I | re.S)
                robots = robots_match.group(1).strip() if robots_match else "index, follow"

                # Persist to DB
                conn = sqlite3.connect(self.db_path)
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO seo_audits (target_key, url, status_code, title, description_len, h1_text, canonical, has_schema, robots, health_score, recommendations)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (key, url, status_code, title, desc_len, h1_text, canonical, has_schema, robots, max(score, 10.0), json.dumps(recs)))
                conn.commit()
                conn.close()

                return {
                    "key": key,
                    "url": url,
                    "status_code": status_code,
                    "title": title,
                    "h1": h1_text,
                    "score": max(score, 10.0),
                    "recs": recs,
                    "keywords": target["primary_keywords"]
                }
        except Exception as e:
            return {
                "key": key,
                "url": url,
                "status_code": 500,
                "score": 0.0,
                "error": str(e),
                "recs": [f"Connection error: {e}"]
            }

    def run_full_smartmag_seo_audit(self):
        results = {}
        for k, v in SMARTMAG_TARGETS.items():
            results[k] = self.audit_target(k, v)
        return results

    def get_summary_report(self):
        audits = self.run_full_smartmag_seo_audit()
        avg_score = sum(a.get("score", 0) for a in audits.values()) / len(audits)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "average_seo_health": round(avg_score, 1),
            "pages_audited": len(audits),
            "targets": audits,
            "action_plan_first_page_rank": [
                "1. Internal Cross-Linking: Link 'store', 'travel', and 'trade' directly from the main publication navigation & footer with keyword-rich anchor text.",
                "2. Programmatic Schema.org Injection: Deploy Organization + WebSite + SearchAction JSON-LD on root, Product schema on /store, TouristTrip on /travel, and SoftwareApplication on trade.",
                "3. Automated Search Engine Pings: Submit /sitemap.xml to Google Search Console & Bing Webmaster API upon daily publishing cycles.",
                "4. Core Web Vitals Optimization: Cache hero graphics, enable Brotli/Gzip compression and preload primary webfonts.",
                "5. Programmatic Topical Authority: Publish daily long-tail comparison and guide articles linking directly to the respective hub."
            ]
        }
        return report

if __name__ == "__main__":
    engine = JarvisSmartMagSEOEngine()
    rep = engine.get_summary_report()
    print(json.dumps(rep, indent=2))
