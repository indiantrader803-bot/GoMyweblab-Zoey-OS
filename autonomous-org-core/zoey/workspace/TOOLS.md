# TOOLS.md — Gomyweblab Autonomous Enterprise Tools

## System Infrastructure
- **Web Service URL**: https://gomyweblab-zoey-os.onrender.com
- **Local Port**: 8088 (HTTP) & 5678 (n8n Workflow Automation)
- **Primary Database**: SQLite `autonomous-org-core/data/gomyweblab_state.db`
- **Telephony**: Twilio Voice Bridge (DTMF Acknowledge "1") + WhatsApp Business API
- **Rust Runtime**: `zoey-agent-core` (Rust crates for character XML and local LLM execution)
- **Memory Runtime**: `zoey-ferbin-core` (Markdown persistent memory + daily activity journal)
