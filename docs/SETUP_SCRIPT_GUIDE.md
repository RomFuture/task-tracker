# Step-by-step guide: creating the setup script

This guide explains how the setup script works and what each part does. Use it to understand or modify `scripts/setup.sh`.

---

## What the script should do (overview)

1. **Check prerequisites** – Python 3 and (optionally) PostgreSQL available.
2. **Create a virtual environment** – so dependencies stay in the project.
3. **Install Python dependencies** – `pip install -r requirements.txt` inside the venv.
4. **Create the database** – `task_tracker` (if it doesn’t exist).
5. **Run migrations** – apply `migrations/001_create_tasks_table.sql`.
6. **Create `.env`** – copy from `.env.example` and remind the user to fill in their credentials.

The script does **not** install PostgreSQL for the user; they must have it installed and running. The script only sets up the project and the database.

---

## Step 1: Script location and shebang

- Create a file `scripts/setup.sh` in the project root.
- First line: `#!/usr/bin/env bash` so the system runs it with Bash.
- Make it executable: `chmod +x scripts/setup.sh`.

---

## Step 2: Go to the project root

- The script should run from the project directory (where `main.py` and `requirements.txt` are).
- Use something like: `cd "$(dirname "$0")/.."` so that running `./scripts/setup.sh` from anywhere still works, or require the user to run it from the project root and use `cd "$(dirname "$0")"` if you prefer.

Common pattern: resolve the directory where the script lives, then go one level up to the project root:

```bash
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"
```

---

## Step 3: Check for Python 3

- Run `python3 --version` or `command -v python3` to see if Python 3 is installed.
- If not, print a message like “Please install Python 3 and run this script again” and exit with code 1.

---

## Step 4: Create virtual environment

- If the `venv` directory does not exist, run: `python3 -m venv venv`.
- If it exists, skip this step (idempotent).

---

## Step 5: Install Python requirements

- Use the venv’s pip so you don’t touch the system Python:  
  `./venv/bin/pip install -r requirements.txt`
- Or on Windows (if you add a `.bat` later): `venv\Scripts\pip install -r requirements.txt`.
- If this fails, exit with a non-zero code and show the error.

---

## Step 6: Check for PostgreSQL (optional but useful)

- Check that `psql` or `createdb` is available: e.g. `command -v psql` or `command -v createdb`.
- If not found, print a warning: “PostgreSQL (psql) not found. Install PostgreSQL, then create the database and run the migration manually (see README).” and continue anyway so the user at least has the venv and .env.

---

## Step 7: Create the database

- Only if PostgreSQL is available:
  - Create the database if it doesn’t exist. One way:  
    `createdb task_tracker 2>/dev/null || true`  
    so that “database already exists” doesn’t fail the script.
  - Or use `psql -d postgres -c "CREATE DATABASE task_tracker;"` and ignore the error if it already exists.

---

## Step 8: Run the migration

- Run your migration SQL file against the new database:  
  `psql -d task_tracker -f migrations/001_create_tasks_table.sql`
- If the user doesn’t have permission or the DB doesn’t exist, this may fail; the script can print the error and tell them to fix DB access and run the migration manually.

---

## Step 9: Create `.env` from `.env.example`

- If `.env` does not exist, copy: `cp .env.example .env`.
- Then print a reminder: “Edit .env and set DB_USER and DB_PASSWORD to your PostgreSQL username and password.”
- If `.env` already exists, you can skip copying so you don’t overwrite their credentials.

---

## Step 10: Success message

- Print something like: “Setup complete. Activate the venv with: source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows). Then run: python main.py”

---

## Summary checklist for the script

- [ ] Shebang and executable bit.
- [ ] Change to project root.
- [ ] Check Python 3; exit if missing.
- [ ] Create venv if missing.
- [ ] Install requirements with venv’s pip.
- [ ] Check for psql/createdb; warn if missing.
- [ ] Create database `task_tracker` if possible.
- [ ] Run migration SQL.
- [ ] Copy `.env.example` to `.env` if `.env` doesn’t exist.
- [ ] Print next steps (activate venv, edit .env, run main.py).

---

## Notes for users running the script

- **PostgreSQL:** Must be installed and the server running. The script does not install PostgreSQL.
- **Username and password:** Come from the user’s own PostgreSQL setup (e.g. the `postgres` user or a user they created). They put these in `.env` after the script runs.
- **Windows:** The guide and script focus on Bash (Linux/Mac). For Windows you can add a `scripts/setup.bat` or recommend WSL/Git Bash and running `bash scripts/setup.sh`.
