# Browser Task Runner

A modular browser automation framework built with Python and Playwright. It automates common web interactions such as login, screenshots, scraping, and file downloads, with built-in logging, exports, and HTML reporting.

## Objectives

- Automate repetitive browser tasks via simple CLI commands
- Provide reusable, modular components for browser automation
- Generate structured outputs (screenshots, data exports, downloads)
- Log all activity and generate HTML reports for audit trails

## Project Structure

```text
browser-task-runner/
├── automate.py          # Entry point — run with: python automate.py {task}
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
├── venv/                # Virtual environment (isolated Python + Playwright)
│
├── core/                # Reusable core modules
│   ├── browser.py       # Playwright browser instance management
│   ├── cli.py           # CLI argument parsing
│   ├── dispatcher.py    # Task routing/dispatch logic
│   ├── exporter.py      # Data export helpers (e.g., CSV)
│   ├── logger.py        # Logging configuration
│   ├── reports.py       # HTML report generation
│   └── utils.py         # General utility functions
│
├── config/              # Project configuration
│   └── settings.py      # Central settings (URLs, credentials, paths)
│
├── tasks/               # Runnable task implementations
│   ├── __init__.py
│   ├── download.py      # File download automation
│   ├── login.py         # Login flow automation
│   ├── open_site.py     # Open a website
│   ├── screenshot.py    # Screenshot capture
│   └── scrape.py        # Web scraping
│
├── reports/             # Generated HTML report files
├── outputs/             # Generated outputs
│   ├── screenshots/     # Captured screenshots (.png)
│   ├── exports/         # Exported data files (.csv)
│   └── downloads/       # Downloaded files
└── logs/                # Log files
    └── automation.log   # Application log
```

## Setup

```bash
python -m venv venv

pip install -r requirements.txt

playwright install
```

## Usage

Run any task by passing its name as an argument:

```bash
python automate.py {task}
```

### Available Tasks

| Command      | Description                     |
|--------------|---------------------------------|
| `open`       | Open a target website           |
| `login`      | Automate login on a test site   |
| `screenshot` | Capture a screenshot of a page  |
| `scrape`     | Scrape data from a page         |
| `download`   | Download a file from a page     |
