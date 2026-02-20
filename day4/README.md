# Day 4 — Shell Scripting & Process Management

- `deploy_monitor.py` — run and monitor multiple deployment commands (parallel/sequential)
- `exercises_day4.py` — subprocess, signal, multiprocessing examples

Example:
`python deploy_monitor.py --cmd "sleep 1 && echo ok" --cmd "echo hello" --parallel --timeout 5`
