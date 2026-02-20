"""Day 4 exercises — subprocess, signal handling, multiprocessing (minimal)
- run_cmd: run a shell command
- handle_signal_demo: register a SIGINT handler
- parallel_map_example: simple multiprocessing Pool example
"""
import multiprocessing
import os
import signal
import subprocess
import time


def run_cmd(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True)


def handle_signal_demo():
    def handler(signum, frame):
        print('Got signal', signum)
        raise SystemExit(0)
    signal.signal(signal.SIGINT, handler)
    print('Press Ctrl+C to trigger handler (sleeping 5s)')
    time.sleep(5)


def parallel_map_example(nums):
    with multiprocessing.Pool(4) as p:
        return p.map(lambda x: x * x, nums)


if __name__ == '__main__':
    print(run_cmd('echo hello').stdout)
    try:
        handle_signal_demo()
    except SystemExit:
        print('Exit from signal demo')
    print('parallel map:', parallel_map_example([1,2,3,4]))
