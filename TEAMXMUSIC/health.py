import os
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'TeamX Music Bot is running'}, 200

@app.route('/')
def root():
    return {'status': 'ok', 'message': 'TeamX Music Bot Health Check Service'}, 200

def run_health_server():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

def start_health_server():
    """Start the health server in a separate thread"""
    health_thread = threading.Thread(target=run_health_server, daemon=True)
    health_thread.start()
    return health_thread
