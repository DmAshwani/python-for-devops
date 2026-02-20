# 1-Week Python Learning Plan: DevOps Perspective
*A Senior Mentor's Guide to Python for DevOps Engineers*

---

## Day 1: Python Basics & CLI Fundamentals

### Core Concepts
- **Python Syntax Essentials**: Variables, data types (int, str, list, dict, tuple, set), operators
- **Control Flow**: if/elif/else, loops (for, while), break, continue, pass
- **Functions**: Definition, parameters, return values, *args, **kwargs
- **Modules & Imports**: Standard library overview, importing built-in modules
- **Virtual Environments**: venv, purpose, and creation
- **Command-line Arguments**: sys.argv, argparse module for robust CLI tools

### Exercises for Practice
1. Write a Python script that accepts command-line arguments and prints them
2. Create a calculator function that handles multiple operations
3. Build a utility to parse and display system information
4. Create a simple CLI tool using argparse with subcommands

### Scenario-Based Questions
1. *Your team runs several one-off scripts in production. How would you structure a Python script to make it reusable and maintainable?*
2. *A junior dev creates a script with hardcoded values. How would you refactor it to accept CLI arguments?*
3. *You need to create a tool that works across different environments (dev, staging, prod). How would you handle configuration?*

### Daily Project: System Information CLI Tool
**Objective**: Create a CLI tool that displays system information

**Requirements**:
- Accept arguments: `--cpu`, `--memory`, `--disk`, `--all`
- Use `argparse` for command-line parsing
- Display formatted output
- Make it executable from anywhere in the system

**Example Usage**:
```bash
python sysinfo.py --cpu
python sysinfo.py --all
```

---

## Day 2: File & System Operations

### Core Concepts
- **File I/O**: Open, read, write, seek, context managers (with statement)
- **os Module**: File/directory operations, environment variables, path manipulation
- **pathlib Module**: Modern approach to path handling (replacement for os.path)
- **subprocess Module**: Running system commands, capturing output, error handling
- **Exception Handling**: try/except/finally, custom exceptions
- **Logging**: Configuring loggers, log levels, handlers

### Exercises for Practice
1. Write functions to read/parse configuration files (INI, text format)
2. Create a script that recursively finds and processes files by extension
3. Execute shell commands from Python and capture output
4. Implement error handling and logging in a script
5. Compare pathlib vs os.path with practical examples

### Scenario-Based Questions
1. *A deployment script fails silently. How would you add comprehensive logging and error handling?*
2. *You need to recursively copy files but skip certain directories. What's your approach?*
3. *Your script needs to run different system commands on Linux vs Windows. How do you handle this?*

### Daily Project: Log Analyzer Tool
**Objective**: Create a tool to parse and analyze application logs

**Requirements**:
- Read log files from a directory
- Filter by log level (ERROR, WARNING, INFO)
- Search for specific patterns/keywords
- Generate a summary report
- Export filtered logs to a new file
- Include proper error handling and logging

**Example Output**:
```
Total Lines: 1500
Errors: 45
Warnings: 120
Info: 1335
Top 5 Error Messages: [...]
```

---

## Day 3: Working with APIs & HTTP Requests

### Core Concepts
- **requests Module**: GET, POST, PUT, DELETE, headers, authentication
- **JSON Processing**: json module, parsing responses, handling nested data
- **Error Handling**: HTTP status codes, timeouts, retries
- **API Authentication**: Basic auth, tokens, API keys
- **Response Validation**: Status codes, content-type verification
- **Rate Limiting**: Implementing backoff strategies

### Exercises for Practice
1. Make GET requests to a public API and parse JSON response
2. Handle different HTTP status codes appropriately
3. Implement retry logic with exponential backoff
4. Create a function that validates API responses
5. Work with authentication (bearer tokens, API keys)

### Scenario-Based Questions
1. *Your deployment script needs to call an external API to fetch configuration. How do you handle timeouts and failures?*
2. *An API endpoint is rate-limited. How would you implement a retry strategy?*
3. *You need to integrate with multiple APIs with different authentication methods. How do you structure this?*

### Daily Project: Service Health Check Tool
**Objective**: Create a monitoring tool that checks health of multiple services via APIs

**Requirements**:
- Accept a list of endpoints (from file or CLI)
- Check each endpoint's health (GET request)
- Implement timeout and retry logic
- Log results with timestamps
- Generate a simple status report (UP/DOWN)
- Send alerts for failed services (simulate with logging)

**Example Configuration**:
```
services.json:
{
  "services": [
    {"name": "API", "url": "http://api.example.com/health"},
    {"name": "Database", "url": "http://db.example.com:8080/status"}
  ]
}
```

---

## Day 4: Shell Scripting & Process Management

### Core Concepts
- **subprocess Advanced**: Popen, pipes, communication, process management
- **Signal Handling**: Signal module, graceful shutdowns
- **Environment Variables**: Reading, setting, passing to subprocesses
- **Shell Integration**: Writing Python scripts that work like shell scripts
- **Multiprocessing vs Threading**: Use cases, Pool, Queue
- **Process Monitoring**: Getting process info, resource usage

### Exercises for Practice
1. Create a wrapper script that executes multiple shell commands sequentially
2. Implement a process monitor that shows running processes
3. Handle signals for graceful shutdown
4. Use multiprocessing to parallelize tasks
5. Create a Python script that logs all environment variables

### Scenario-Based Questions
1. *You need to parallelize a deployment across multiple servers. How do you use Python's multiprocessing?*
2. *A long-running process needs to gracefully handle SIGTERM. How do you implement this?*
3. *Your script must work with CI/CD pipelines and respect their environment. What do you need to consider?*

### Daily Project: Deployment Pipeline Monitor
**Objective**: Create a tool that monitors and manages multiple deployment processes

**Requirements**:
- Execute multiple deployment commands in parallel or sequential mode
- Monitor process output in real-time
- Capture and log both stdout and stderr
- Handle signals (SIGTERM) for graceful shutdown
- Generate a summary report with success/failure status
- Implement timeout handling per process

**Example Usage**:
```bash
python deploy_monitor.py --parallel config.yaml
python deploy_monitor.py --sequential config.yaml --timeout 300
```

---

## Day 5: Configuration Management & Data Formats

### Core Concepts
- **JSON Processing**: dumps, loads, pretty printing, custom encoders
- **YAML Handling**: PyYAML library, parsing, validation
- **INI Files**: configparser module
- **Environment Variables**: python-dotenv for .env files
- **TOML**: Modern configuration format (Python 3.11+)
- **Configuration Validation**: Schema validation, defaults, type checking

### Exercises for Practice
1. Write a config loader that supports multiple formats (JSON, YAML, INI)
2. Implement config validation with meaningful error messages
3. Create a config merger that supports overrides and defaults
4. Handle sensitive data in config files (passwords, tokens)
5. Build a config template generator

### Scenario-Based Questions
1. *Your application needs configuration from multiple sources (file, env vars, CLI). How do you merge them with proper precedence?*
2. *Team members accidentally commit secrets to the config file. How do you prevent this?*
3. *You need to validate that all required config values are present before starting. What's your approach?*

### Daily Project: Configuration Management System
**Objective**: Build a configuration loader supporting multiple formats with validation

**Requirements**:
- Support JSON, YAML, and INI formats
- Merge configurations from multiple sources (file + environment variables)
- Implement schema validation (required fields, types, ranges)
- Support environment variable substitution in config values
- Generate default config templates
- Detect and warn about deprecated config options

**Example**:
```yaml
# Config file
database:
  host: ${DB_HOST}  # Substituted from env
  port: 5432
  username: admin
  # password should NOT be here!
```

---

## Day 6: Containerization & Infrastructure Concepts

### Core Concepts
- **Docker Basics**: Understanding containers, images, Dockerfile concepts
- **Interacting with Docker**: docker-py library, building images, running containers
- **Kubernetes Client**: kubernetes Python client basics
- **Infrastructure as Code**: Representing infrastructure in Python
- **Service Discovery**: Basic concepts and implementation
- **Configuration for Different Environments**: Dev, staging, production

### Exercises for Practice
1. Write Python code to build and run Docker containers
2. Implement a simple container health checker
3. Create a tool to manage multiple containers
4. Write code to query Kubernetes cluster information
5. Build an environment configurator (dev/staging/prod)

### Scenario-Based Questions
1. *You need to programmatically build Docker images as part of your CI/CD pipeline. How do you do this in Python?*
2. *Your Python application needs to run inside a container. What considerations for dependencies, logging, and signals?*
3. *You want to create multiple container instances with different configurations. How would you manage this?*

### Daily Project: Container Manager Tool
**Objective**: Create a tool to manage Docker containers for local development

**Requirements**:
- Build Docker images from Dockerfile
- Run/stop/remove containers programmatically
- Execute commands inside containers
- View container logs
- Network containers together
- Export container configuration to YAML
- Multi-environment support (dev/test/prod configurations)

**Example Usage**:
```bash
python container_manager.py build --name myapp
python container_manager.py run --name myapp --env dev
python container_manager.py logs myapp --tail 50
```

---

## Day 7: Automation & Monitoring

### Core Concepts
- **Scheduling Tasks**: schedule library, APScheduler, cron concepts
- **Health Checks**: Building robust health check endpoints
- **Metrics & Monitoring**: Prometheus client, sending metrics
- **Alerting**: Webhook integrations, email notifications
- **Automation Patterns**: Event-driven automation, triggers
- **Best Practices**: Error recovery, idempotency, observability

### Exercises for Practice
1. Create a scheduler that runs tasks at specific intervals
2. Build a health check system with multiple checks
3. Implement metrics collection and exposure
4. Create alert notifications via webhooks
5. Build a retry mechanism with exponential backoff

### Scenario-Based Questions
1. *You need to run a cleanup task every night. How do you schedule it and ensure it completes successfully?*
2. *Your automated process fails occasionally. How do you make it resilient with retries and alerting?*
3. *You need to expose application health and metrics for monitoring. What's your approach?*

### Daily Project: Automation & Monitoring Suite
**Objective**: Create a comprehensive automation and monitoring system

**Requirements**:
- Schedule daily/weekly tasks (backups, cleanup, reports)
- Implement comprehensive health checks (disk space, memory, external services)
- Expose metrics endpoint (simulated Prometheus format)
- Send alerts to webhook/email on failures
- Track execution history and generate reports
- Implement graceful error handling with notifications
- Create dashboard data (JSON endpoint with current status)

**Example**:
```bash
python automation_suite.py start
# Runs scheduled tasks
# Exposes /metrics endpoint
# Sends alerts on failures
# Maintains execution history
```

---

## Weekly Practice: Build an End-to-End DevOps Tool

After completing all 7 days, you're ready for a comprehensive project:

**Project**: Automated Backup & Recovery Manager

**Integrate learnings from all 7 days**:
- Day 1: CLI interface with argparse
- Day 2: File operations for backup/restore
- Day 3: External API calls for cloud backup status
- Day 4: Multiprocessing for parallel backups
- Day 5: YAML config for backup policies
- Day 6: Docker containerization of the tool
- Day 7: Scheduled execution and monitoring

**Minimum Requirements**:
- Define backup policies in YAML
- Execute backups with retry logic
- Monitor backup health
- Send notifications on completion/failure
- Generate backup reports
- Containerize the solution
- Schedule automatic backups

---

## Learning Tips from a Senior DevOps Engineer

1. **Write code for operations, not just features**
   - Always include logging
   - Handle errors gracefully
   - Make scripts idempotent
   - Test edge cases

2. **Focus on reliability**
   - Implement retries with backoff
   - Add timeouts
   - Monitor resources
   - Know when your code fails

3. **Embrace infrastructure thinking**
   - Configuration management is critical
   - Secrets should never be in code
   - Environments matter (dev/staging/prod)
   - Observability is not optional

4. **Practice automation patterns**
   - Deployments should be repeatable
   - Avoid manual steps
   - Monitor what matters
   - Alert on actionable issues

5. **Study real-world tools**
   - Review how tools like Ansible, Terraform handle similar problems
   - Learn from open-source DevOps tools
   - Understand containerization deeply
   - Keep current with industry standards

---

## Resources for Deeper Dives

- **Standard Library**: Official Python docs for modules covered
- **Requests**: https://docs.python-requests.org/
- **PyYAML**: https://pyyaml.org/wiki/PyYAMLDocumentation
- **Docker SDK**: https://docker-py.readthedocs.io/
- **Kubernetes Python Client**: https://github.com/kubernetes-client/python
- **APScheduler**: https://apscheduler.readthedocs.io/

---

**Remember**: The goal isn't to become a Python expert, but to develop practical skills that make you more effective in DevOps. Each day builds on the previous, and the projects reinforce learning through practice.

---

## Implementation in this repository ✅
The daily projects and exercise solutions have been implemented under the following folders:

- `day1/` — `sysinfo.py`, `exercises_day1.py`
- `day2/` — `log_analyzer.py`, `exercises_day2.py`
- `day3/` — `health_check.py`, `exercises_day3.py`
- `day4/` — `deploy_monitor.py`, `exercises_day4.py`
- `day5/` — `config_loader.py`, `exercises_day5.py`
- `day6/` — `container_manager.py`, `exercises_day6.py`
- `day7/` — `automation_suite.py`, `exercises_day7.py`

Each folder contains a short README and minimal, runnable scripts (no external dependencies unless explicitly noted). Run the `README.md` inside a day's folder for quick usage examples.

Good luck! 🚀
