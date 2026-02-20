#!/usr/bin/env python3
"""Deployment Pipeline Monitor (Day 4)

Features (minimal):
- Run multiple shell commands sequentially or in parallel
- Capture stdout/stderr and exit codes
- Per-command timeout
- Graceful shutdown on SIGINT/SIGTERM

Usage:
  python deploy_monitor.py --cmd "sleep 1 && echo ok" --cmd "echo hello" --parallel
"""
import argparse
import concurrent.futures
import shlex
import signal
import subprocess
import threading
import time

shutdown_flag = threading.Event()


def _run_command(cmd, timeout=None):
    if shutdown_flag.is_set():
        return {'cmd': cmd, 'status': 'skipped'}
    try:
        proc = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return {'cmd': cmd, 'returncode': proc.returncode, 'stdout': proc.stdout.strip(), 'stderr': proc.stderr.strip()}
    except subprocess.TimeoutExpired:
        return {'cmd': cmd, 'status': 'timeout'}
    except Exception as e:
        return {'cmd': cmd, 'status': 'error', 'error': str(e)}


def _signal_handler(signum, frame):
    print('Received signal', signum, '- shutting down gracefully...')
    shutdown_flag.set()


def run_commands(commands, parallel=False, timeout=None):
    results = []
    if parallel:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(8, len(commands))) as ex:
            futures = [ex.submit(_run_command, c, timeout) for c in commands]
            for f in concurrent.futures.as_completed(futures):
                results.append(f.result())
    else:
        for c in commands:
            if shutdown_flag.is_set():
                results.append({'cmd': c, 'status': 'skipped'})
                continue
            results.append(_run_command(c, timeout))
    return results


def main():
    signal.signal(signal.SIGINT, _signal_handler)
    signal.signal(signal.SIGTERM, _signal_handler)

    p = argparse.ArgumentParser()
    p.add_argument('--cmd', action='append', required=True, help='Shell command to run (can repeat)')
    p.add_argument('--parallel', action='store_true')
    p.add_argument('--timeout', type=int, help='Per-command timeout in seconds')
    args = p.parse_args()

    start = time.time()
    results = run_commands(args.cmd, parallel=args.parallel, timeout=args.timeout)
    elapsed = time.time() - start

    print('\nSummary (elapsed: %.2fs):' % elapsed)
    for r in results:
        print('-', r)


if __name__ == '__main__':
    main()
