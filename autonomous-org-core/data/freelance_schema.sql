BEGIN TRANSACTION;
CREATE TABLE client_conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deal_ref TEXT NOT NULL,
        sender TEXT NOT NULL, -- 'CLIENT' or 'AGENT:<AgentName>'
        message_text TEXT NOT NULL,
        intent TEXT, -- 'INQUIRY', 'COUNTER_OFFER', 'FEEDBACK', 'APPROVAL'
        decision_applied TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(deal_ref) REFERENCES freelance_deals(deal_ref)
    );
CREATE TABLE freelance_deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        deal_ref TEXT UNIQUE,
        platform TEXT NOT NULL, -- Upwork, Fiverr, Freelancer, Direct
        client_name TEXT NOT NULL,
        client_country TEXT,
        project_title TEXT NOT NULL,
        project_description TEXT,
        client_budget REAL,
        market_benchmark_rate REAL,
        negotiated_budget REAL,
        current_stage TEXT NOT NULL,
        -- Stages: SCOUTED -> PROPOSAL_SENT -> IN_NEGOTIATION -> CONTRACT_AWARDED -> BUILDING -> DEMO_DEPLOYED -> FEEDBACK_REFINEMENT -> FINAL_HANDOVER -> PAID
        demo_url TEXT,
        client_feedback TEXT,
        handover_repo TEXT,
        confidence_score REAL DEFAULT 0.95,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "freelance_deals" VALUES(6,'FL-40813331','Freelancer.com (Live API)','Client ID: None','Global','Independent developers for public-sector software projects 2027 (remote)','Steelgaard Oy, a Finnish company, bids for public-sector software, web and data contracts in the EU,',36.0,45.0,41.4,'SCOUTED',NULL,NULL,NULL,0.95,'2026-11-11 14:19:27','2026-11-11 14:19:27');
INSERT INTO "freelance_deals" VALUES(7,'FL-40813376','Freelancer.com (Live API)','Client ID: None','Global','Development of a Modern, Fast & SEO-Friendly Marathi Government Jobs and Exam Updates Website','We are looking for an experienced web developer to build a professional, lightweight, mobile-friendl',11000.0,13750.0,1.264999999999999818e+04,'SCOUTED',NULL,NULL,NULL,0.95,'2026-11-11 14:19:27','2026-11-11 14:19:27');
INSERT INTO "freelance_deals" VALUES(8,'FL-40813369','Freelancer.com (Live API)','Client ID: None','Global','Bold Colourful Website Revamp -- 2','My website needs a complete visual refresh that instantly grabs attention and feels vibrant, modern,',200.0,250.0,2.299999999999999716e+02,'SCOUTED',NULL,NULL,NULL,0.95,'2026-11-11 14:19:27','2026-11-11 14:19:27');
INSERT INTO "freelance_deals" VALUES(9,'FL-40808922','Freelancer.com (Live API)','Client ID: None','Global','Truck Income Risk ML Mentor','I’m building a web platform that estimates how risky a truck’s income is and I need a seasoned machi',225.0,281.25,258.75,'SCOUTED',NULL,NULL,NULL,0.95,'2026-11-11 14:19:27','2026-11-11 14:19:27');
INSERT INTO "freelance_deals" VALUES(10,'FL-40813336','Freelancer.com (Live API)','Client ID: None','Global','Faith-Based Blessings Blog Writing','I’m commissioning an uplifting blog article that shows readers how blessings flow through faith and ',20.0,25.0,23.0,'SCOUTED',NULL,NULL,NULL,0.95,'2026-11-11 14:19:27','2026-11-11 14:19:27');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('freelance_deals',10);
INSERT INTO "sqlite_sequence" VALUES('client_conversations',8);
COMMIT;
