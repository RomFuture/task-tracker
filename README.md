# Task Tracker (CLI)

A command-line task tracker that stores tasks in **PostgreSQL**. Add, list, update, delete, and change task status from the terminal.

## Features

- **Add** tasks with a description
- **List** all tasks or filter by status (`todo`, `in_progress`, `done`)
- **Update** a task’s description
- **Delete** a task
- **Mark** a task as in progress or done
- Errors shown in the menu above the command prompt
- Data stored in PostgreSQL with migrations

## Tech stack

- **Python 3**
- **PostgreSQL**
- **psycopg2** (DB driver), **python-dotenv** (config)

## Prerequisites

- **Python 3**
- **PostgreSQL** installed and running (server must be started, e.g. `sudo systemctl start postgresql`)

## Quick setup (recommended)

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd task-tracker
   ```

2. **Run the setup script** (Linux/macOS)
   ```bash
   ./scripts/setup.sh
   ```
   This will:
   - Create a virtual environment (`venv`)
   - Install Python dependencies from `requirements.txt`
   - Create the `task_tracker` database (if PostgreSQL is available)
   - Run the migration to create the `tasks` table
   - Copy `.env.example` to `.env` if `.env` doesn’t exist

3. **Edit `.env`** with your PostgreSQL credentials:
   - `DB_USER` – your PostgreSQL username (e.g. `postgres` or a user you created)
   - `DB_PASSWORD` – that user’s password  
   Use the same credentials you use to connect with `psql`.

4. **Activate the virtual environment and run the app**
   ```bash
   source venv/bin/activate   # Linux/macOS
   python main.py
   ```

## Manual setup

If you prefer not to use the script:

1. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database and run the migration**
   ```bash
   createdb task_tracker
   psql -d task_tracker -f migrations/001_create_tasks_table.sql
   ```

4. **Configure environment**
   - Copy `.env.example` to `.env`
   - Set `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT` in `.env`

5. **Run the app**
   ```bash
   python main.py
   ```

## Usage

Once the app is running, use these commands at the prompt:

| Command | Description |
|--------|-------------|
| `add <description>` | Add a new task |
| `list` | Show all tasks |
| `list-status <status>` | Show tasks with status `todo`, `in_progress`, or `done` |
| `update <id> <description>` | Change a task’s description |
| `delete <id>` | Remove a task |
| `mark-in-progress <id>` | Set task status to in progress |
| `mark-done <id>` | Set task status to done |
| `exit` | Quit the app |

## Project structure

```
task-tracker/
├── main.py              # CLI entry point and menu
├── requirements.txt     # Python dependencies
├── .env.example         # Template for DB config (copy to .env)
├── services/
│   ├── db.py            # Database connection
│   ├── task_service.py  # Task operations (add, list, update, etc.)
│   └── view.py          # Format and print task list
├── migrations/
│   └── 001_create_tasks_table.sql   # Creates tasks table
├── scripts/
│   └── setup.sh         # Setup script (venv, DB, migration, .env)
└── docs/
    └── SETUP_SCRIPT_GUIDE.md    # How the setup script works
```

## Notes

- **`.env`** is not committed (it’s in `.gitignore`). Each developer uses their own PostgreSQL user and password in `.env`.
- For more detail on the setup script, see [docs/SETUP_SCRIPT_GUIDE.md](docs/SETUP_SCRIPT_GUIDE.md).
