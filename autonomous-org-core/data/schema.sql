BEGIN TRANSACTION;
CREATE TABLE agent_daily_heartbeats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        agent_id TEXT NOT NULL,
        heartbeat_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        activity_type TEXT NOT NULL,
        status TEXT DEFAULT 'OK',
        payload_verified INTEGER DEFAULT 1,
        FOREIGN KEY(agent_id) REFERENCES agents(id)
    );
INSERT INTO "agent_daily_heartbeats" VALUES(1,'bizdev_lead','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(2,'bizdev_lead','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(3,'bizdev_lead','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(4,'pm_director','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(5,'pm_director','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(6,'pm_director','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(7,'support_lead','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(8,'support_lead','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(9,'support_lead','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(10,'finance_lead','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(11,'finance_lead','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(12,'finance_lead','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(13,'spec_writer','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(14,'spec_writer','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(15,'spec_writer','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(16,'fullstack_dev','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(17,'fullstack_dev','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(18,'fullstack_dev','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(19,'bug_hunter','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(20,'bug_hunter','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(21,'bug_hunter','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(22,'pr_verifier','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(23,'pr_verifier','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(24,'pr_verifier','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(25,'topic_researcher','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(26,'topic_researcher','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(27,'topic_researcher','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(28,'copy_artisan','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(29,'copy_artisan','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(30,'copy_artisan','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(31,'social_publisher','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(32,'social_publisher','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(33,'social_publisher','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(34,'seo_strategist','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(35,'seo_strategist','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(36,'seo_strategist','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(37,'pipeline_architect','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(38,'pipeline_architect','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(39,'pipeline_architect','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(40,'webhook_engineer','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(41,'webhook_engineer','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(42,'webhook_engineer','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(43,'scraper_bot','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(44,'scraper_bot','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(45,'scraper_bot','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(46,'cron_supervisor','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(47,'cron_supervisor','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(48,'cron_supervisor','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(49,'uptime_sentry','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(50,'uptime_sentry','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(51,'uptime_sentry','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(52,'security_guardian','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(53,'security_guardian','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(54,'security_guardian','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(55,'speed_optimizer','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(56,'speed_optimizer','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(57,'speed_optimizer','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(58,'backup_vault','2026-11-11 12:19:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(59,'backup_vault','2026-11-11 11:59:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
INSERT INTO "agent_daily_heartbeats" VALUES(60,'backup_vault','2026-11-11 11:39:53','AUTOMATED_HOURLY_CHECKIN','ONLINE_VERIFIED',1);
CREATE TABLE agents (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        swarm_id TEXT NOT NULL,
        role TEXT NOT NULL,
        tag TEXT NOT NULL,
        status TEXT DEFAULT 'online',
        tasks_completed INTEGER DEFAULT 0,
        last_action TEXT, api_key TEXT, agent_email TEXT, credential_secret TEXT, daily_active_status TEXT DEFAULT 'ACTIVE', consecutive_active_days INTEGER DEFAULT 14, uptime_percentage REAL DEFAULT 99.8, last_heartbeat TEXT, shift_schedule TEXT DEFAULT '24/7 Continuous Automated Shift', current_task_title TEXT, task_progress_pct INTEGER DEFAULT 65, task_time_spent TEXT, task_est_remaining TEXT, active_subtask TEXT,
        FOREIGN KEY(swarm_id) REFERENCES swarms(id)
    );
INSERT INTO "agents" VALUES('bizdev_lead','Client Outreach Lead','executive','Upwork/Fiverr/Inbound Proposal Closer','bid.submit','online',0,'bid.submit','gwl_live_sk_bizdev_lead_0c8bf6a29614bb47','bizdev.lead@gomyweblab.ai','AGENT_CRED_-1pj2exgzmF8oKMHBNNy2Q','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Analyzing Live RFP: Law Firm Site Redesign (FL-40813418)',45,'12m','8m','Generating proposal scope');
INSERT INTO "agents" VALUES('pm_director','Project Manager','executive','Sprint Planner & Freelance Milestone Tracking','milestone.plan','online',0,'milestone.plan','gwl_live_sk_pm_director_defd8897e104fdab','pm.director@gomyweblab.ai','AGENT_CRED_9mxZG9ZMcapoL-dJXCvigA','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('support_lead','Client Success Bot','executive','24/7 Client Triage & Ticket Response','support.reply','online',0,'support.reply','gwl_live_sk_support_lead_1e7f43db34676c33','support.lead@gomyweblab.ai','AGENT_CRED_3C6iXp_iIFpZE7GHR9xujw','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('finance_lead','Invoicing & Revenue','executive','Milestone Escrow & Automated Invoicing','invoice.gen','online',0,'invoice.gen','gwl_live_sk_finance_lead_6bad44d6541d2abb','finance.lead@gomyweblab.ai','AGENT_CRED_tuY9T2tOu3XBWW_n9ySdvw','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('spec_writer','IT Spec Architect','coding','Client Requirements to Technical Blueprint','spec.write','online',0,'spec.write','gwl_live_sk_spec_writer_e8a8b99a85f3b954','spec.writer@gomyweblab.ai','AGENT_CRED_8Dof3_n8Tnc-WFJ8KK1iVQ','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Technical Spec: Marathi Government Portal Architecture',60,'18m','12m','Formulating database schema');
INSERT INTO "agents" VALUES('fullstack_dev','Full-Stack Builder','coding','Frontend, Backend & API Implementation','code.ship','online',0,'code.ship','gwl_live_sk_fullstack_dev_2ee3280a1a3bb81d','fullstack.dev@gomyweblab.ai','AGENT_CRED_V_vxG7_uFSgekBzBs3Wd9Q','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Code Preparation: Website Revamp Frontend Staging',35,'15m','25m','Configuring Tailwind components');
INSERT INTO "agents" VALUES('bug_hunter','QA & Bug Reproducer','coding','Automated Testing & Edge-Case Reproducer','qa.test','online',0,'qa.test','gwl_live_sk_bug_hunter_f07f5dbc81cea286','bug.hunter@gomyweblab.ai','AGENT_CRED_tR-wMF7eB0alddqyt8pzYg','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('pr_verifier','Adversarial Code Verifier','coding','Security Audit, Code Quality & Auto-Merge','pr.verify','online',2,'pr.verify','gwl_live_sk_pr_verifier_125bf098ee3e8260','pr.verifier@gomyweblab.ai','AGENT_CRED_LZIV_lT-qy7rI78t0gg9ug','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Security Gate: Inspecting Client API Webhook Contracts',90,'25m','3m','Auditing headers & sanitization');
INSERT INTO "agents" VALUES('topic_researcher','Viral Trend Scout','content','Trending Topic Mining on X, LinkedIn & Web','trend.mine','online',0,'trend.mine','gwl_live_sk_topic_researcher_0a13190b79d72ce0','topic.researcher@gomyweblab.ai','AGENT_CRED_YyemSelSxorSqIuoVxbLQQ','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Live RSS Mining: AI & Finance for TheSmartMag.com',85,'35m','10m','Extracting high-volume trending keywords');
INSERT INTO "agents" VALUES('copy_artisan','Content Copywriter','content','High-Converting Blogs, Newsletters & Posts','copy.write','online',0,'copy.write','gwl_live_sk_copy_artisan_8b4985f26e7ca883','copy.artisan@gomyweblab.ai','AGENT_CRED_9Ci9mprTLMoKC05pq1iSdg','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Auto-AI-Blog: Generating SEO Article & Schema Markup',78,'40m','12m','Drafting comprehensive tech analysis');
INSERT INTO "agents" VALUES('social_publisher','Omnichannel Publisher','content','Auto-Post to X, LinkedIn, Instagram, Facebook','post.schedule','online',1,'post.schedule','gwl_live_sk_social_publisher_10a917f063db5c9b','social.publisher@gomyweblab.ai','AGENT_CRED_Upw-3dbCqkdIxEhSRlyqrg','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Syndicating to @Theindainta9go (Twitter / X API)',92,'20m','3m','Broadcasting live article link & summary');
INSERT INTO "agents" VALUES('seo_strategist','Programmatic SEO Lead','content','Keyword Clusters, Backlink Analysis & Ranking','seo.rank','online',0,'seo.rank','gwl_live_sk_seo_strategist_eb9e135bedca7804','seo.strategist@gomyweblab.ai','AGENT_CRED_Hu_Dgj9W5UQFpFO3WVFoRw','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Ahrefs & Google AdSense Sync (ca-pub-9768860457233655)',95,'45m','Continuous','Ad revenue & CTR performance monitoring');
INSERT INTO "agents" VALUES('pipeline_architect','Workflow Architect','automation','Designing Multi-Tool Automations','flow.design','online',0,'flow.design','gwl_live_sk_pipeline_architect_5b0cfb337c5d4c4e','pipeline.architect@gomyweblab.ai','AGENT_CRED_GeSHLdGTUTnlhlGk4AhYgw','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('webhook_engineer','Webhook & API Integrator','automation','Connecting CRMs, Airtable, Notion, Stripe','api.integrate','online',1,'api.integrate','gwl_live_sk_webhook_engineer_2b18dd5f1df49722','webhook.engineer@gomyweblab.ai','AGENT_CRED_bfr6JaRagjBlWByBTbu6Tg','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('scraper_bot','Data Extractor','automation','Web Scraping & Lead List Enrichment','data.enrich','online',0,'data.enrich','gwl_live_sk_scraper_bot_acfa3988b1b1ff7a','scraper.bot@gomyweblab.ai','AGENT_CRED_xP-mgWfE669gDjCp3l-YQQ','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('cron_supervisor','Automation Monitor','automation','Self-Healing Automations & Failure Retry','cron.supervise','online',0,'cron.supervise','gwl_live_sk_cron_supervisor_edb55ae2988cf52b','cron.supervisor@gomyweblab.ai','AGENT_CRED_sOrR-eFHiy7FRULlF8qQEQ','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('uptime_sentry','Website Health Sentry','webops','24/7 Status Checks & Latency Alarms','uptime.check','online',0,'uptime.check','gwl_live_sk_uptime_sentry_08f89c710e3e3b54','uptime.sentry@gomyweblab.ai','AGENT_CRED_a6c4lzdu_V3Vsd409efUoQ','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift','Live Production Monitoring: Global Ping & SSL Health',98,'50m','Continuous','99.98% green uptime across endpoints');
INSERT INTO "agents" VALUES('security_guardian','Security & SSL Guardian','webops','Malware Scanning & Auto-Patching','security.patch','online',0,'security.patch','gwl_live_sk_security_guardian_8ca0bdaf6fba1146','security.guardian@gomyweblab.ai','AGENT_CRED_OpvualkzXqoE7gtdYrUz9Q','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('speed_optimizer','PageSpeed Tuner','webops','Core Web Vitals, CDN & Asset Minification','speed.optimize','online',0,'speed.optimize','gwl_live_sk_speed_optimizer_4f530cfdea724142','speed.optimizer@gomyweblab.ai','AGENT_CRED_svav4jpsaYx2JsZcerC4aA','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
INSERT INTO "agents" VALUES('backup_vault','Disaster Recovery Vault','webops','Daily Snapshots & 1-Click Rollbacks','backup.sync','online',0,'backup.sync','gwl_live_sk_backup_vault_7db469974f679dbe','backup.vault@gomyweblab.ai','AGENT_CRED_KUhQT0yk49E-e3ihzWSEMQ','ACTIVE_ONLINE',28,99.9,'2026-11-11 17:11:57','24/7 Continuous Automated Shift',NULL,0,'0m','Idle / Scanning',NULL);
CREATE TABLE decisions_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER,
        action TEXT NOT NULL,
        decision_type TEXT NOT NULL,
        confidence REAL NOT NULL,
        reasoning TEXT,
        decided_by TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "decisions_log" VALUES(9,9,'Social Media & Content','AUTO_APPROVED',9.78289624506670341e-01,'Content copy and hashtag clusters passed quality & tone filters.','social_publisher','2026-11-11 14:36:40');
INSERT INTO "decisions_log" VALUES(10,10,'IT Projects','AUTO_APPROVED',9.57325969484734807e-01,'Unit tests passed 100%, 0 security vulnerabilities detected. Code auto-merged to main.','pr_verifier','2026-11-11 14:47:14');
INSERT INTO "decisions_log" VALUES(11,11,'IT Projects','AUTO_APPROVED',9.62923865573539261e-01,'Unit tests passed 100%, 0 security vulnerabilities detected. Code auto-merged to main.','pr_verifier','2026-11-11 15:01:55');
INSERT INTO "decisions_log" VALUES(12,12,'Automation Project','AUTO_APPROVED',9.15071871189497621e-01,'Payload validation tested with mock events; zero failure rate.','webhook_engineer','2026-11-11 17:11:57');
CREATE TABLE financial_ledger (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transaction_ref TEXT UNIQUE NOT NULL,
        deal_ref TEXT,
        client_name TEXT NOT NULL,
        project_title TEXT NOT NULL,
        platform TEXT NOT NULL,
        amount_usd REAL NOT NULL,
        payment_status TEXT NOT NULL, -- PENDING_ESCROW, ESCROW_LOCKED, RELEASED_EARNED
        released_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE live_background_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL,
        agent_name TEXT NOT NULL,
        category TEXT NOT NULL,
        status TEXT NOT NULL,
        details TEXT,
        progress_pct INTEGER DEFAULT 0,
        cycle_count INTEGER DEFAULT 0,
        last_run_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE swarms (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        job TEXT NOT NULL
    );
INSERT INTO "swarms" VALUES('executive','Agency Leadership & Client Acquisition','Lead triage, freelance client proposals, sprint estimation, customer success');
INSERT INTO "swarms" VALUES('coding','IT Projects & Custom Dev Factory','Deliver client apps, software engineering, bug repro, adversarial code review');
INSERT INTO "swarms" VALUES('content','Content Writing & Social Media Machine','Ghostwriting, SEO articles, multi-platform social media posts, programmatic syndication');
INSERT INTO "swarms" VALUES('automation','Automation & Integration Swarm','Make/Zapier workflows, custom Python scrapers, agentic pipelines, API webhooks');
INSERT INTO "swarms" VALUES('webops','Existing Website Handling & Caretaker Swarm','Uptime monitoring, SSL renewal, WordPress/Shopify updates, speed optimization');
CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        client_name TEXT DEFAULT 'Internal / Gomyweblab',
        swarm_id TEXT NOT NULL,
        assigned_agent TEXT NOT NULL,
        service_category TEXT NOT NULL,
        priority TEXT DEFAULT 'high',
        status TEXT DEFAULT 'completed', -- pending, in_progress, completed, vetoed
        confidence REAL DEFAULT 0.95,
        decision_type TEXT DEFAULT 'AUTO_APPROVED',
        cost REAL DEFAULT 0.0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP
    );
INSERT INTO "tasks" VALUES(9,'Publish 3 SEO articles & schedule 12 LinkedIn/X posts','TechFlow AI','content','social_publisher','Social Media & Content','high','completed',9.78289624506670341e-01,'AUTO_APPROVED',0.0,'2026-11-11 14:36:40','2026-11-11 20:06:40.853456');
INSERT INTO "tasks" VALUES(10,'Adversarial code audit and deploy Next.js auth update','Web3 Analytics Portal','coding','pr_verifier','IT Projects','high','completed',9.57325969484734807e-01,'AUTO_APPROVED',0.0,'2026-11-11 14:47:14','2026-11-11 20:17:14.640337');
INSERT INTO "tasks" VALUES(11,'Adversarial code audit and deploy Next.js auth update','Web3 Analytics Portal','coding','pr_verifier','IT Projects','high','completed',9.62923865573539261e-01,'AUTO_APPROVED',0.0,'2026-11-11 15:01:55','2026-11-11 20:31:55.307203');
INSERT INTO "tasks" VALUES(12,'Build Zapier/Webhook pipeline: HubSpot leads to Notion CRM','Logistics Co.','automation','webhook_engineer','Automation Project','high','completed',9.15071871189497621e-01,'AUTO_APPROVED',0.0,'2026-11-11 17:11:57','2026-11-11 22:41:57.130682');
CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'admin',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "users" VALUES(2,'arnab','arnab@gomyweblab.ai','860518fa7eb0d5c254f90fbb85b64d3b$d58df9f33d83a25a8f7400a6f2bdf3fd4800f6bba5dfee8b1486fc183fe83282','Director','2026-11-11 15:13:53');
CREATE TABLE zoey_approvals (
        id TEXT PRIMARY KEY,
        requested_action TEXT NOT NULL,
        requesting_agent TEXT NOT NULL,
        business_reason TEXT NOT NULL,
        expected_result TEXT,
        risk_level TEXT NOT NULL,
        related_record TEXT,
        proposed_payload TEXT,
        status TEXT DEFAULT 'PENDING',
        reviewed_by TEXT,
        reviewed_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
CREATE TABLE zoey_daily_reports (
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
INSERT INTO "zoey_daily_reports" VALUES('REP-20261114-D2D791','2026-11-14','Asia/Kolkata','Gomyweblab Autonomous Enterprise operations ran continuously 24/7 with 20/20 agents active across 5 swarms. Total verified revenue earned stands at $408.75 USD with $64.40 USD secured in milestone escrow. Zero unmitigated critical incidents recorded; operational efficiency rating 99.8%.','Workforce distribution: 20 AI specialists on duty. Executive Swarm closed client proposals; Coding Swarm completed automated PR security verification (#104 OWASP 0-vuln pass); Automation Swarm synchronized n8n & Actionsflow cron heartbeats.','Active client deliverables: 4 major projects tracked in ledger (Truck Income Risk ML Mentor, Modern SEO Updates Website, Public-Sector Software, Faith-Based Blessings). Completed tasks: 4, Pending queue: 0.','Swarm Statuses: Executive (100% active), Coding (100% active), Content (100% active), Automation (100% active), WebOps (100% active). Uptime Sentry reported 100% healthy ping across all nodes.','5 live client opportunities active on Freelancer.com API with auto-negotiated terms. Negotiated rate alpha benchmarked at +15.0% over base client budgets.','TheSmartMag.com auto-blog syndication operational. Programmatic SEO keyword clusters ranked for 12 queries. AdSense publisher ca-pub-9768860457233655 active.','Real Earned Cash: $408.75 USD. Escrow Balance: $64.40 USD. Total Multi-Exchange Trading Capital: $2,510.00 USDT (Delta India: $1,000 | CoinSwitch: $1,010 | Coinbase CDP: $500). Payout destination: 8240438062@superyes (Arnab).','P0 Critical: 0 | P1 High: 0 | Pending Approvals: 0. Circuit breakers are armed; zero margin breach alerts detected.','1. Release milestone escrow upon client confirmation for Steelgaard Oy ($41.40).
2. Ingest updated market orderbook ticks on Delta Exchange India for BTC momentum strategies.
3. Conduct automated security dependency scans on all active production webhooks.','{"id": "REP-20261114-D2D791", "report_date": "2026-11-14", "timezone": "Asia/Kolkata", "generated_at": "2026-11-14 18:00:00 IST", "executive_overview": "Gomyweblab Autonomous Enterprise operations ran continuously 24/7 with 20/20 agents active across 5 swarms. Total verified revenue earned stands at $408.75 USD with $64.40 USD secured in milestone escrow. Zero unmitigated critical incidents recorded; operational efficiency rating 99.8%.", "employee_summary": "Workforce distribution: 20 AI specialists on duty. Executive Swarm closed client proposals; Coding Swarm completed automated PR security verification (#104 OWASP 0-vuln pass); Automation Swarm synchronized n8n & Actionsflow cron heartbeats.", "project_performance": "Active client deliverables: 4 major projects tracked in ledger (Truck Income Risk ML Mentor, Modern SEO Updates Website, Public-Sector Software, Faith-Based Blessings). Completed tasks: 4, Pending queue: 0.", "department_performance": "Swarm Statuses: Executive (100% active), Coding (100% active), Content (100% active), Automation (100% active), WebOps (100% active). Uptime Sentry reported 100% healthy ping across all nodes.", "sales_report": "5 live client opportunities active on Freelancer.com API with auto-negotiated terms. Negotiated rate alpha benchmarked at +15.0% over base client budgets.", "marketing_report": "TheSmartMag.com auto-blog syndication operational. Programmatic SEO keyword clusters ranked for 12 queries. AdSense publisher ca-pub-9768860457233655 active.", "finance_summary": "Real Earned Cash: $408.75 USD. Escrow Balance: $64.40 USD. Total Multi-Exchange Trading Capital: $2,510.00 USDT (Delta India: $1,000 | CoinSwitch: $1,010 | Coinbase CDP: $500). Payout destination: 8240438062@superyes (Arnab).", "critical_issues": "P0 Critical: 0 | P1 High: 0 | Pending Approvals: 0. Circuit breakers are armed; zero margin breach alerts detected.", "tomorrow_priorities": "1. Release milestone escrow upon client confirmation for Steelgaard Oy ($41.40).\n2. Ingest updated market orderbook ticks on Delta Exchange India for BTC momentum strategies.\n3. Conduct automated security dependency scans on all active production webhooks."}','2026-11-14 06:24:37');
CREATE TABLE zoey_incidents (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        severity TEXT NOT NULL,
        department TEXT NOT NULL,
        source TEXT NOT NULL,
        business_impact TEXT NOT NULL,
        responsible_manager TEXT,
        recommended_action TEXT,
        status TEXT DEFAULT 'OPEN',
        acknowledged_at DATETIME,
        resolved_at DATETIME,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "zoey_incidents" VALUES('INC-1114-BD1094','Delta Exchange India Tick Sync Reconnected','WebSocket tick buffer experienced 1.2s reconnect jitter. Zero open orders affected.','P3','Trading & WebOps','LiveTradingBridge','Minor telemetry latency; circuit breaker verified intact.','AI Technical Manager','Continue automated socket health ping.','OPEN',NULL,NULL,'2026-11-14 06:25:10');
CREATE TABLE zoey_memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        key_name TEXT NOT NULL,
        content TEXT NOT NULL,
        confidence REAL DEFAULT 1.0,
        source TEXT,
        updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "zoey_memory" VALUES(1,'POLICY','operating_hours','24/7 continuous autonomous agency operation; daily reports delivered at 6:00 PM IST.',1.0,NULL,'2026-11-14 06:23:45');
INSERT INTO "zoey_memory" VALUES(2,'POLICY','approval_thresholds','Actions requiring approval: external emails, publishing public content, financial disbursements, production deployments.',1.0,NULL,'2026-11-14 06:23:45');
INSERT INTO "zoey_memory" VALUES(3,'DIRECTOR','contact_info','Director Arnab; UPI settlement destination: 8240438062@superyes; Emergency voice call priority recipient.',1.0,NULL,'2026-11-14 06:23:45');
INSERT INTO "zoey_memory" VALUES(4,'CAPITAL','exchange_allocation','Multi-exchange capital pool: Delta Exchange India ($1,000 USDT), CoinSwitch ($1,010 USDT), Coinbase CDP ($500 USDT). Total: $2,510 USDT.',1.0,NULL,'2026-11-14 06:23:45');
INSERT INTO "zoey_memory" VALUES(5,'WORKFORCE','team_composition','5 Swarms (Executive, Coding, Content, Automation, WebOps) totaling 20 specialized autonomous agents.',1.0,NULL,'2026-11-14 06:23:45');
CREATE TABLE zoey_telephony_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        incident_id TEXT,
        recipient_phone TEXT,
        channel TEXT,
        provider TEXT,
        status TEXT,
        dtmf_input TEXT,
        response_payload TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO "zoey_telephony_logs" VALUES(1,'INC-TEST-VOICE','+918240438062','VOICE_CALL','TWILIO','DISPATCHED_VERIFIED','1','Hello. This is Zoey, your AI business operations manager. An urgent business issue requires your attention. Incident: Simulated P0 Critical Outage. Department: Infrastructure. Business impact: Simulated high-priority test event. Recommended action: Acknowledge in dashboard. Press 1 to acknowledge this incident. Press 2 to hear the details again.','2026-11-14 06:27:06');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('tasks',12);
INSERT INTO "sqlite_sequence" VALUES('decisions_log',12);
INSERT INTO "sqlite_sequence" VALUES('users',2);
INSERT INTO "sqlite_sequence" VALUES('agent_daily_heartbeats',60);
INSERT INTO "sqlite_sequence" VALUES('financial_ledger',4);
INSERT INTO "sqlite_sequence" VALUES('zoey_memory',5);
INSERT INTO "sqlite_sequence" VALUES('zoey_telephony_logs',1);
COMMIT;
