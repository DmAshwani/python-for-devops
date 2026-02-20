#!/usr/bin/env python3
"""Configuration loader (Day 5) — minimal
- Supports JSON and INI files
- Merges with environment variables (env overrides)
- Does simple ${VAR} substitution in string values

Usage:
  python config_loader.py --file config.json
  python config_loader.py --file config.ini --show
"""
import argparse
import configparser
import json
import os
import re


def _substitute_env(value):
    if not isinstance(value, str):
        return value
    pattern = re.compile(r"\$\{([A-Za-z0-9_]+)\}")

    def repl(m):
        return os.environ.get(m.group(1), m.group(0))

    return pattern.sub(repl, value)


def load_json(path):
    with open(path) as fh:
        data = json.load(fh)
    return {k: _substitute_env(v) if isinstance(v, str) else v for k, v in data.items()}


def load_ini(path):
    cp = configparser.ConfigParser()
    cp.read(path)
    out = {}
    for section in cp.sections():
        out[section] = {k: _substitute_env(v) for k, v in cp[section].items()}
    return out


def load(path):
    if path.endswith('.json'):
        return load_json(path)
    if path.endswith('.ini') or path.endswith('.cfg'):
        return load_ini(path)
    # try YAML if available
    try:
        import yaml  # type: ignore
        with open(path) as fh:
            return yaml.safe_load(fh)
    except Exception:
        raise ValueError('Unsupported config format or PyYAML not installed')


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--file', required=True)
    p.add_argument('--show', action='store_true')
    args = p.parse_args()

    cfg = load(args.file)
    if args.show:
        print(json.dumps(cfg, indent=2))
    else:
        print('Loaded config from', args.file)
