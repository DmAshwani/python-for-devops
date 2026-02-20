"""Day 7 exercises — scheduling & monitoring (minimal)
- simple_scheduler: run a function every N seconds
- send_alert: simulated webhook alert (prints)
"""
import threading
import time


def simple_scheduler(fn, every, stop_after=5):
    end = time.time() + stop_after
    while time.time() < end:
        fn()
        time.sleep(every)


def send_alert(message, dest='webhook://example'):
    print('ALERT ->', dest, message)


if __name__ == '__main__':
    def task():
        print('task run', time.time())
    simple_scheduler(task, 1, stop_after=3)
    send_alert('test alert')
