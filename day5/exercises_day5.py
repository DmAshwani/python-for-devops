"""Day 5 exercises — configuration formats (minimal)
- merge_configs: simple precedence (env > file)
- validate_required: basic validation
"""
import os
import json


def merge_configs(file_cfg, env_prefix='APP_'):
    out = dict(file_cfg)
    for k, v in os.environ.items():
        if k.startswith(env_prefix):
            out_key = k[len(env_prefix):].lower()
            out[out_key] = v
    return out


def validate_required(cfg, keys):
    missing = [k for k in keys if k not in cfg or cfg[k] in (None, '')]
    if missing:
        raise ValueError('Missing required config keys: ' + ','.join(missing))
    return True


if __name__ == '__main__':
    print('merge example:', merge_configs({'host': 'localhost'}))
    try:
        validate_required({'host': 'x'}, ['host', 'port'])
    except ValueError as e:
        print('validation failed (expected):', e)
