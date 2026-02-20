"""Day 3 exercises — HTTP requests (minimal)
- simple_get: GET using urllib
- retry_example: minimal retry wrapper
"""
import urllib.request
import urllib.error
import time


def simple_get(url, timeout=5):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, r.read(200)
    except Exception as e:
        return None, str(e)


def retry_get(url, retries=3, delay=1):
    for i in range(retries):
        status, data = simple_get(url)
        if status:
            return status
        time.sleep(delay)
    return None


if __name__ == '__main__':
    print(simple_get('https://httpbin.org/get'))
    print('retry ->', retry_get('https://httpbin.org/status/200'))
