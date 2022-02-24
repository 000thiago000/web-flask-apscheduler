# Web-Flask-Apscheduler

Web-Flask-APScheduler is an extension of Flask-APScheduler that adds a web interface to APScheduler.

## Installing

Install it inside a `virtualenv` to make things easier:

```bash
python3 -m venv .
source ./bin/activate
pip install -r requirements.txt
```
## Usage

Copy `app/sample-jobs.py` as `app/jobs.py` and configure your scheduler jobs.

Run command before first use to create sqlite.db

```bash
python db.py
```

To run the scheduler:

```bash
python main.py
```
