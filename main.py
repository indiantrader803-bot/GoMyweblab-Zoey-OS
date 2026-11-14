"""
WSGI / ASGI Production Bridge for GoMyweblab & Zoey AI on Render
"""

import os
import sys
import threading
from http.server import HTTPServer

# Add core and zoey paths
CORE_DIR = os.path.join(os.path.dirname(__file__), "autonomous-org-core")
AGENTS_DIR = os.path.join(CORE_DIR, "agents")
ZOEY_DIR = os.path.join(CORE_DIR, "zoey")
sys.path.append(CORE_DIR)
sys.path.append(AGENTS_DIR)
sys.path.append(ZOEY_DIR)

from server import GomyweblabHttpHandler

def run_app():
    port = int(os.environ.get("PORT", 8088))
    server = HTTPServer(('0.0.0.0', port), GomyweblabHttpHandler)
    print(f"GoMyWebLab & Zoey OS Live Server listening on 0.0.0.0:{port}")
    server.serve_forever()

if __name__ == '__main__':
    run_app()
