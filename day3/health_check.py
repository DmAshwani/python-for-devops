#!/usr/bin/env python3
"""Service Health Check Tool (Day 3)

Usage:
  python health_check.py --endpoints https://example.com/health https://httpbin.org/status/200
  python health_check.py --file endpoints.txt
"""
import argparse
import json
import time
import urllib.request
import urllib.error


def check_url(url, timeout=3, retries=2, backoff=1.5):
    attempt = 0
    while True:
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'health-check/1.0'})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return True, r.status
        except urllib.error.HTTPError as e:
            return False, e.code
        except Exception as e:
            attempt += 1
            if attempt > retries:
                return False, str(e)
            time.sleep(backoff ** attempt)


def load_endpoints_from_file(path):
    with open(path) as fh:
        return [l.strip() for l in fh if l.strip()]


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--endpoints', nargs='*', help='List of endpoints to check')
    p.add_argument('--file', help='File containing endpoints (one per line)')
    args = p.parse_args()

    urls = args.endpoints or []
    if args.file:
        urls.extend(load_endpoints_from_file(args.file))

    if not urls:
        p.print_help()
        return

    results = {}
    for u in urls:
        ok, code = check_url(u)
        results[u] = {'ok': ok, 'status': code}
        print(u, '->', 'UP' if ok else 'DOWN', code)

    print('\nSummary:')
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
