"""Day 6 exercises — container interaction (minimal)
- check_docker: verify docker CLI
- build_via_cli: run docker build via subprocess
"""
import shutil
import subprocess


def check_docker():
    return shutil.which('docker') is not None


def build_via_cli(tag, path='.'):
    return subprocess.run(['docker', 'build', '-t', tag, path], capture_output=True, text=True)


if __name__ == '__main__':
    print('docker available:', check_docker())
