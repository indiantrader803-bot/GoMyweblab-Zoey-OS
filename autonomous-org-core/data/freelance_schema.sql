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
INSERT INTO "client_conversations" VALUES(9,'FL-40817533','ZOEY:Proposal Bot','Hi there,

I reviewed your project requirement: "Fast, Editable PDF-to-Word Conversion". Our team specializes in full-stack Python engineering, workflow automation, and custom web applications, delivering clean, production-grade solutions that strictly match your functional criteria.

### Proposed Execution Strategy & Milestones:
1. **Phase 1: Architecture & Data Model:** Immediate setup of the core logic, schema, and API interface within 24 hours.
2. **Phase 2: Core Development & Automation:** Full implementation with unit tests to ensure 100% bug-free behavior.
3. **Phase 3: Client Review & Staging Preview:** We provide a live staging demo URL so you can inspect and test the deliverable firsthand.
4. **Phase 4: Deployment & Final Handover:** Clean codebase delivery with clear setup documentation and deployment assistance.

### Commercials:
- **Proposed Bid:** $19.00 USD
- **Estimated Delivery:** 3 Days

We are ready to start immediately. Feel free to open a chat so we can discuss the specific details and launch the first milestone!

Best regards,
Arnab & The Autonomous Engineering Team','PROPOSAL_DRAFT','READY_TO_SUBMIT','2026-11-14 07:13:43');
INSERT INTO "client_conversations" VALUES(10,'FL-40817544','ZOEY:Proposal Bot','Hi there,

I reviewed your project requirement: "Financial Reconciliation Desktop App". Our team specializes in full-stack Python engineering, workflow automation, and custom web applications, delivering clean, production-grade solutions that strictly match your functional criteria.

### Proposed Execution Strategy & Milestones:
1. **Phase 1: Architecture & Data Model:** Immediate setup of the core logic, schema, and API interface within 24 hours.
2. **Phase 2: Core Development & Automation:** Full implementation with unit tests to ensure 100% bug-free behavior.
3. **Phase 3: Client Review & Staging Preview:** We provide a live staging demo URL so you can inspect and test the deliverable firsthand.
4. **Phase 4: Deployment & Final Handover:** Clean codebase delivery with clear setup documentation and deployment assistance.

### Commercials:
- **Proposed Bid:** $133.00 USD
- **Estimated Delivery:** 3 Days

We are ready to start immediately. Feel free to open a chat so we can discuss the specific details and launch the first milestone!

Best regards,
Arnab & The Autonomous Engineering Team','PROPOSAL_DRAFT','READY_TO_SUBMIT','2026-11-14 07:13:43');
INSERT INTO "client_conversations" VALUES(11,'FL-40817537','ZOEY:Proposal Bot','Hi there,

I reviewed your project requirement: "Automated VPN Subscription Platform Development". Our team specializes in full-stack Python engineering, workflow automation, and custom web applications, delivering clean, production-grade solutions that strictly match your functional criteria.

### Proposed Execution Strategy & Milestones:
1. **Phase 1: Architecture & Data Model:** Immediate setup of the core logic, schema, and API interface within 24 hours.
2. **Phase 2: Core Development & Automation:** Full implementation with unit tests to ensure 100% bug-free behavior.
3. **Phase 3: Client Review & Staging Preview:** We provide a live staging demo URL so you can inspect and test the deliverable firsthand.
4. **Phase 4: Deployment & Final Handover:** Clean codebase delivery with clear setup documentation and deployment assistance.

### Commercials:
- **Proposed Bid:** $194.75 USD
- **Estimated Delivery:** 5 Days

We are ready to start immediately. Feel free to open a chat so we can discuss the specific details and launch the first milestone!

Best regards,
Arnab & The Autonomous Engineering Team','PROPOSAL_DRAFT','READY_TO_SUBMIT','2026-11-14 07:13:43');
INSERT INTO "client_conversations" VALUES(12,'UP-41222','ZOEY:Upwork Autopilot','Hi there,

I read your project "Python Developer for REST API Integration & Automation" and would love to deliver this for you. With strong expertise across Python, workflow orchestration, and modern web application development, I can implement your requirements cleanly with full test coverage.

### Key Highlights:
- Architecture & Data Layer setup within 24 hours.
- Clean, modular codebase adhering strictly to industry standards.
- Live demo staging provided for your review before final release.

Proposed Budget: $450.00 | Delivery: 4 Days.

Best regards,
Arnab Laha','UPWORK_PROPOSAL','READY_IN_PORTAL','2026-11-14 07:27:02');
INSERT INTO "client_conversations" VALUES(13,'UP-41223','ZOEY:Upwork Autopilot','Hi there,

I read your project "Full-Stack Web App (FastAPI / Next.js) with Authentication" and would love to deliver this for you. With strong expertise across Python, workflow orchestration, and modern web application development, I can implement your requirements cleanly with full test coverage.

### Key Highlights:
- Architecture & Data Layer setup within 24 hours.
- Clean, modular codebase adhering strictly to industry standards.
- Live demo staging provided for your review before final release.

Proposed Budget: $850.00 | Delivery: 4 Days.

Best regards,
Arnab Laha','UPWORK_PROPOSAL','READY_IN_PORTAL','2026-11-14 07:27:02');
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
INSERT INTO "freelance_deals" VALUES(11,'FL-40817533','Freelancer.com','Verified Client','Global','Fast, Editable PDF-to-Word Conversion',NULL,15.0,25.0,19.0,'DRAFTED_WINNING_BID','https://www.freelancer.com/projects/adobe-acrobat/Fast-Editable-PDF-Word-Conversion',NULL,NULL,0.98,'2026-11-14 07:13:43','2026-11-14 07:13:43');
INSERT INTO "freelance_deals" VALUES(12,'FL-40817544','Freelancer.com','Verified Client','Global','Financial Reconciliation Desktop App',NULL,30.0,250.0,133.0,'DRAFTED_WINNING_BID','https://www.freelancer.com/projects/pandas/Financial-Reconciliation-Desktop-App',NULL,NULL,0.98,'2026-11-14 07:13:43','2026-11-14 07:13:43');
INSERT INTO "freelance_deals" VALUES(13,'FL-40817537','Freelancer.com','Verified Client','Global','Automated VPN Subscription Platform Development',NULL,200.0,210.0,194.75,'DRAFTED_WINNING_BID','https://www.freelancer.com/projects/nodejs/Automated-VPN-Subscription-Platform',NULL,NULL,0.98,'2026-11-14 07:13:43','2026-11-14 07:13:43');
INSERT INTO "freelance_deals" VALUES(14,'UP-41222','Upwork','Enterprise US Client','United States','Python Developer for REST API Integration & Automation',NULL,450.0,517.5,450.0,'PROPOSAL_DRAFTED','https://www.upwork.com',NULL,NULL,0.96,'2026-11-14 07:27:02','2026-11-14 07:27:02');
INSERT INTO "freelance_deals" VALUES(15,'UP-41223','Upwork','FinTech Startup','United Kingdom','Full-Stack Web App (FastAPI / Next.js) with Authentication',NULL,850.0,9.77499999999999886e+02,850.0,'PROPOSAL_DRAFTED','https://www.upwork.com',NULL,NULL,0.96,'2026-11-14 07:27:02','2026-11-14 07:27:02');
INSERT INTO "freelance_deals" VALUES(16,'ST-the-raenest-glob','SuperteamDAO Earn','Superteam DAO Sponsor','Global (Solana)','The Raenest Global Bounty - Writing, Video & Animation Bounty',NULL,13000.0,13000.0,13000.0,'BOUNTY_OPEN','https://earn.superteam.fun/listings/bounties/the-raenest-global-bounty-writing-video-and-animation',NULL,NULL,0.99,'2026-11-14 07:31:05','2026-11-14 07:31:05');
INSERT INTO "freelance_deals" VALUES(17,'ST-startup-village-','SuperteamDAO Earn','Superteam DAO Sponsor','Global (Solana)','Startup Village Chitwan - Gaida Race',NULL,100.0,100.0,100.0,'BOUNTY_OPEN','https://earn.superteam.fun/listings/bounties/startup-village-chitwan-gaida-race',NULL,NULL,0.99,'2026-11-14 07:31:05','2026-11-14 07:31:05');
INSERT INTO "freelance_deals" VALUES(18,'ST-chimp-on-metaple','SuperteamDAO Earn','Superteam DAO Sponsor','Global (Solana)','Write a thread on $CHIMP Fair Launch - Part 1',NULL,500.0,500.0,500.0,'BOUNTY_OPEN','https://earn.superteam.fun/listings/bounties/chimp-on-metaplex',NULL,NULL,0.99,'2026-11-14 07:31:05','2026-11-14 07:31:05');
INSERT INTO "freelance_deals" VALUES(19,'ST-make-a-video-abo','SuperteamDAO Earn','Superteam DAO Sponsor','Global (Solana)','Make a video about our x402 Feature',NULL,500.0,500.0,500.0,'BOUNTY_OPEN','https://earn.superteam.fun/listings/bounties/make-a-video-about-our-x402-feature',NULL,NULL,0.99,'2026-11-14 07:31:05','2026-11-14 07:31:05');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('freelance_deals',19);
INSERT INTO "sqlite_sequence" VALUES('client_conversations',13);
COMMIT;
