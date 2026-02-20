#!/usr/bin/env python3
"""System Information CLI Tool (Day 1)

Usage examples:
  python sysinfo.py --cpu
  python sysinfo.py --memory
  python sysinfo.py --disk
  python sysinfo.py --all
"""
import argparse
import os
import platform
import shutil
import sys


def cpu_info():
    return {"logical_cpus": os.cpu_count(), "architecture": platform.machine()}


def memory_info():
    # Linux-specific /proc/meminfo fallback; graceful if not present
    info = {}
    try:
        if sys.platform == "linux":
            with open('/proc/meminfo') as f:
                for line in f:
                    if line.startswith('MemTotal'):
                        info['total_kb'] = int(line.split(':')[1].strip().split()[0])
                        break
        else:
            info['note'] = 'Platform-specific memory info not available'
    except Exception as e:
        info['error'] = str(e)
    return info


def disk_info(path="/"):
    try:
        du = shutil.disk_usage(path)
        return {"total": du.total, "used": du.used, "free": du.free}
    except Exception as e:
        return {"error": str(e)}


def main():
    p = argparse.ArgumentParser(description='System information CLI')
    p.add_argument('--cpu', action='store_true')
    p.add_argument('--memory', action='store_true')
    p.add_argument('--disk', action='store_true')
    p.add_argument('--all', action='store_true')
    p.add_argument('--path', default='/', help='Path to inspect for disk usage')
    args = p.parse_args()

    if not (args.cpu or args.memory or args.disk or args.all):
        p.print_help()
        return

    if args.cpu or args.all:
        print('CPU:')
        print(cpu_info())
        print()

    if args.memory or args.all:
        print('Memory:')
        print(memory_info())
        print()

    if args.disk or args.all:
        print('Disk:')
        print(disk_info(args.path))


if __name__ == '__main__':
    main()
