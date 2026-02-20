"""Day 1 exercises (minimal solutions)
- echo_args: print CLI args
- calculator: simple calculator function
- argparse_subcmd: example of argparse subcommands
"""
import argparse
import sys


def echo_args():
    print('Arguments:', sys.argv[1:])


def calculator(a, b, op):
    if op == 'add':
        return a + b
    if op == 'sub':
        return a - b
    if op == 'mul':
        return a * b
    if op == 'div':
        return a / b
    raise ValueError('unknown op')


def argparse_subcmd():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='cmd')
    add = sub.add_parser('add')
    add.add_argument('x', type=int)
    add.add_argument('y', type=int)

    args = p.parse_args()
    if args.cmd == 'add':
        print(args.x + args.y)


if __name__ == '__main__':
    # quick demo if run directly
    echo_args()
    print('calc 4+5 =', calculator(4, 5, 'add'))
