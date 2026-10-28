# Intelligent Log Parser & Alerter

## Description
A Python-based log parser that scans server log files for specific keywords such as ERROR, FAILED, and CRITICAL. It saves matching log entries into an incident report and records execution status and errors using Python logging.

## Features
- Search server logs using specific keywords.
- Filter matching log entries.
- Generate an incident report automatically.
- Handle missing input files using exception handling.
- Record application events using Python logging.
- Support command-line arguments using argparse.
- Log a warning when no matching keyword is found.

## Technologies Used
- Python 3
- argparse
- logging
- File Handling
- Exception Handling
- Git and GitHub

## Project Structure
```text
intelligent-log-parser/
├── log_Parser.py
├── server.log
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/solanki-palak123/intelligent-log-parser.git
```

### 2. Navigate to the project directory
```bash
cd intelligent-log-parser
```

### 3. Run the parser
```bash
python3 log_Parser.py --keyword ERROR
```

Replace `ERROR` with another supported keyword, such as `FAILED` or `CRITICAL`.

## Output
Matching log entries are saved to `incident_report.txt`.

Execution details and warnings are recorded in `parser.log`.

## Error Handling
The application handles missing input files and logs a warning when no matching keyword is found.

## Author
Palak Singh
