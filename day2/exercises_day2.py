"""Day 2 exercises — File & System Operations (minimal solutions)
- read_config: read a simple INI-style config
- find_files_by_ext: recursively find files by extension
- run_shell_cmd: execute a shell command and capture output
"""
import configparser
import os
import subprocess


def read_config(path):
    cp = configparser.ConfigParser()
    cp.read(path)
    return {s: dict(cp[s]) for s in cp.sections()}


def find_files_by_ext(root, ext):
    matches = []
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            if fn.endswith(ext):
                matches.append(os.path.join(dirpath, fn))
    return matches


def run_shell_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


if __name__ == '__main__':
    print('Example config read:', read_config('example.ini') if os.path.exists('example.ini') else {})
    print('Find .py files:', find_files_by_ext('.', '.py')[:5])
    code, out, err = run_shell_cmd('echo hello')
    print('run_shell_cmd:', code, out.strip())
