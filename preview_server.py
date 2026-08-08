"""Local preview helper for the Kaifa Lu static portfolio.

Run from this folder:
    python preview_server.py
Then open http://localhost:8000 in a browser.
"""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

PORT = 8000
ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
print(f"Serving {ROOT} at http://localhost:{PORT}")
print("Press Ctrl+C to stop.")
ThreadingHTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler).serve_forever()
