# Task Tracker (CLI)

A command-line tool for managing tasks. Data is stored in PostgreSQL. Add, delete, update tasks and change their status — all from the terminal.

<img width="575" height="325" alt="image" src="https://github.com/user-attachments/assets/dcd24a49-8d6e-4357-b528-1f8074083eff" />

#### What it does


<details>
<summary>Click to expand app features</summary>

<br>

+ Add tasks with a description
+ List all tasks or filter by status (`todo`, `in_progress`, `done`)
+ Update task description
+ Delete tasks
+ Change status to `in_progress` or `done`
+ Errors are shown in the menu above the input prompt
+ Data lives in PostgreSQL, schema is created via migrations
</details>


#### Prerequisites
> [!IMPORTANT]  
> **Python 3** and **PostgreSQL** must be installed (and PostgreSQL must be running when you use the app).

## Quick start

1. **Clone**
   ```bash
   git clone https://github.com/RomFuture/task-tracker
   cd task-tracker
   ```

2. **Run the setup script** (Linux/macOS)
   ```bash
   ./scripts/setup.sh
   ```
   The script will create a `venv`, install dependencies, create the `task_tracker` database (if PostgreSQL is available), run the migration, and copy `.env.example` → `.env`.

3. **Fill in your credentials in `.env`**
   - `DB_USER` — your PostgreSQL username (e.g. `postgres`)
   - `DB_PASSWORD` — that user’s password (same as for `psql`)

4. **Start PostgreSQL and open SQL** (when needed)
   ```bash
   ./scripts/start_db.sh
   ```
   This starts the PostgreSQL service and opens `psql -d task_tracker`. Use this if the server was stopped or you want to run SQL by hand.

5. **Run the app**
   ```bash
   source venv/bin/activate
   python main.py
   ```

## Manual setup

If you prefer not to use the setup script:

1. **Create and activate a venv**
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
   Copy `.env.example` to `.env` and set `DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_PORT`.

5. **Start PostgreSQL** (if needed): `./scripts/start_db.sh`

6. **Run the app**
   ```bash
   python main.py
   ```
## Commands

| Command | What it does |
|--------|---------------|
| `add <description>` | Add a task |
| `list` | Show all tasks |
| `list-status <status>` | Show tasks with status `todo`, `in_progress`, or `done` |
| `update <id> <description>` | Change task description |
| `delete <id>` | Delete a task |
| `mark-in-progress <id>` | Set status to in progress |
| `mark-done <id>` | Set status to done |
| `exit` | Quit |

## Project structure
```text
task-tracker/
├── main.py              # CLI entry point and menu
├── requirements.txt
├── .env.example         # Config template (copy to .env)
├── services/
│   ├── db.py            # Database connection
│   ├── task_service.py  # Task operations (add, list, update, etc.)
│   └── view.py          # Format and print task list
├── migrations/
│   └── 001_create_tasks_table.sql
├── scripts/
│   ├── setup.sh         # Venv, deps, DB, migration, .env
│   └── start_db.sh      # Start PostgreSQL and open psql -d task_tracker
└── docs/
    └── SETUP_SCRIPT_GUIDE.md
```
### Stack
> Python 3, PostgreSQL, psycopg2, python-dotenv