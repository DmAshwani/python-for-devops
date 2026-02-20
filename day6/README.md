# Day 6 — Containerization & Infrastructure

- `container_manager.py` — minimal wrapper around the `docker` CLI (build/run/stop/logs)
- `exercises_day6.py` — small helpers to check Docker availability

Example:
`python container_manager.py build --tag myapp:latest --path .`

Note: This script depends on the Docker CLI being installed and available in PATH.
