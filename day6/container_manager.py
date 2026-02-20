#!/usr/bin/env python3
"""Container Manager Tool (Day 6) — minimal wrapper around Docker CLI

Basic commands supported: build, run, stop, rm, logs, exec

Note: This script calls the `docker` CLI. Ensure Docker is installed and the user has permissions.
"""
import argparse
import shutil
import subprocess
import sys


def check_docker_available():
    return shutil.which('docker') is not None


def docker(args_list):
    cmd = ['docker'] + args_list
    return subprocess.run(cmd, capture_output=True, text=True)


def main():
    if not check_docker_available():
        print('docker CLI not found in PATH. Install Docker or run on a host with Docker.')
        sys.exit(1)

    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd', required=True)

    b = sub.add_parser('build')
    b.add_argument('--tag', required=True)
    b.add_argument('--path', default='.')

    r = sub.add_parser('run')
    r.add_argument('--name', required=True)
    r.add_argument('--image', required=True)
    r.add_argument('--detached', action='store_true')

    s = sub.add_parser('stop')
    s.add_argument('--name', required=True)

    rm = sub.add_parser('rm')
    rm.add_argument('--name', required=True)

    l = sub.add_parser('logs')
    l.add_argument('--name', required=True)
    l.add_argument('--tail', type=int, default=100)

    e = sub.add_parser('exec')
    e.add_argument('--name', required=True)
    e.add_argument('--cmd', required=True)

    args = p.parse_args()

    if args.cmd == 'build':
        r = docker(['build', '-t', args.tag, args.path])
        print(r.stdout)
        if r.returncode:
            print(r.stderr)
            sys.exit(r.returncode)

    if args.cmd == 'run':
        cmd = ['run', '--name', args.name]
        if args.detached:
            cmd.append('-d')
        cmd.append(args.image)
        r = docker(cmd)
        print(r.stdout)

    if args.cmd == 'stop':
        r = docker(['stop', args.name])
        print(r.stdout)

    if args.cmd == 'rm':
        r = docker(['rm', args.name])
        print(r.stdout)

    if args.cmd == 'logs':
        r = docker(['logs', '--tail', str(args.tail), args.name])
        print(r.stdout)

    if args.cmd == 'exec':
        # simple exec (no tty)
        r = docker(['exec', args.name] + args.cmd.split())
        print(r.stdout)


if __name__ == '__main__':
    main()
