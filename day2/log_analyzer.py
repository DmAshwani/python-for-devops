#!/usr/bin/env python3
"""Log Analyzer Tool (Day 2)

Usage:
  python log_analyzer.py --dir logs/ --level ERROR --pattern "timeout" --export filtered.log
"""
import argparse
import glob
import os
import re
from collections import Counter


LOG_LEVELS = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


def analyze_logs(path, level=None, pattern=None):
    files = glob.glob(os.path.join(path, '*'))
    total = 0
    counts = Counter()
    matches = []

    level_re = re.compile(r'\b(' + '|'.join(LOG_LEVELS) + r')\b')
    pattern_re = re.compile(pattern, re.IGNORECASE) if pattern else None

    for f in files:
        try:
            with open(f, 'r', errors='ignore') as fh:
                for line in fh:
                    total += 1
                    m = level_re.search(line)
                    if m:
                        counts[m.group(1)] += 1
                        if level and m.group(1) != level:
                            continue
                    if pattern_re and not pattern_re.search(line):
                        continue
                    matches.append(line.rstrip('\n'))
        except IsADirectoryError:
            continue
        except Exception as e:
            print('Error reading', f, e)

    return {'total_lines': total, 'level_counts': dict(counts), 'matches': matches}


def save_matches(matches, dest):
    with open(dest, 'w') as fh:
        for l in matches:
            fh.write(l + '\n')


def main():
    p = argparse.ArgumentParser(description='Analyze logs in a directory')
    p.add_argument('--dir', default='.', help='Directory containing logs')
    p.add_argument('--level', choices=LOG_LEVELS)
    p.add_argument('--pattern', help='Search pattern (regex)')
    p.add_argument('--export', help='File to export filtered logs')
    args = p.parse_args()

    res = analyze_logs(args.dir, level=args.level, pattern=args.pattern)
    print('Total lines scanned:', res['total_lines'])
    print('Counts by level:', res['level_counts'])
    print('Matched lines:', len(res['matches']))
    if args.export and res['matches']:
        save_matches(res['matches'], args.export)
        print('Exported matches to', args.export)


if __name__ == '__main__':
    main()
