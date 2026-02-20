#!/usr/bin/env python3
"""Automation & Monitoring Suite (Day 7) — minimal
- Simple scheduler (interval-based)
- Health checks (disk, memory)
- Exposes a `/metrics` JSON endpoint on HTTP
- Keeps in-memory execution history

Run:
  python automation_suite.py --port 8000

This is a small demo intended for local/practice use.
"""
import argparse
import http.server
import json
import shutil
import socketserver
import threading
import time
from datetime import datetime


HISTORY = []
HISTORY_LOCK = threading.Lock()


def record_event(name, status, detail=None):
    entry = {'time': datetime.utcnow().isoformat() + 'Z', 'task': name, 'status': status, 'detail': detail}
    with HISTORY_LOCK:
        HISTORY.append(entry)
        if len(HISTORY) > 200:
            HISTORY.pop(0)


def check_disk(path='/', warn_percent=90):
    try:
        du = shutil.disk_usage(path)
        used_pct = int(du.used / du.total * 100)
        return {'path': path, 'used_pct': used_pct, 'ok': used_pct < warn_percent}
    except Exception as e:
        return {'error': str(e)}


def sample_task_cleanup():
    # Simulated cleanup
    record_event('cleanup', 'started')
    time.sleep(0.1)
    record_event('cleanup', 'done')


def sample_task_backup():
    record_event('backup', 'started')
    time.sleep(0.2)
    record_event('backup', 'done')


class Scheduler(threading.Thread):
    def __init__(self, interval_seconds=60):
        super().__init__(daemon=True)
        self.interval = interval_seconds
        self.tasks = []  # list of tuples (callable, interval_seconds, last_run)
        self._stop = threading.Event()

    def add_task(self, func, every):
        self.tasks.append({'fn': func, 'every': every, 'last': 0})

    def stop(self):
        self._stop.set()

    def run(self):
        while not self._stop.is_set():
            now = time.time()
            for t in self.tasks:
                if now - t['last'] >= t['every']:
                    try:
                        t['fn']()
                        t['last'] = now
                    except Exception as e:
                        record_event(t['fn'].__name__, 'error', str(e))
            time.sleep(0.5)


class MetricsHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/metrics') or self.path.startswith('/status'):
            resp = {
                'uptime': time.time(),
                'disk': check_disk('/'),
                'history': None,
            }
            with HISTORY_LOCK:
                resp['history'] = list(HISTORY[-20:])
            body = json.dumps(resp).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # quiet the default logging
        return


def run_http_server(port):
    with socketserver.TCPServer(('', port), MetricsHandler) as httpd:
        print('Serving metrics on port', port)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--port', type=int, default=8000)
    args = p.parse_args()

    sched = Scheduler()
    sched.add_task(sample_task_cleanup, every=10)
    sched.add_task(sample_task_backup, every=15)
    sched.start()

    try:
        run_http_server(args.port)
    finally:
        sched.stop()


if __name__ == '__main__':
    main()
