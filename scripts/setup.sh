#!/usr/bin/env bash
# Task Tracker – setup script (Linux/macOS)
# Run from project root: ./scripts/setup.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

echo "=== Task Tracker setup ==="
echo "Project root: $PROJECT_ROOT"
echo ""

# --- Step 1: Check Python 3 ---
if ! command -v python3 &>/dev/null; then
    echo "Error: python3 not found. Please install Python 3 and run this script again."
    exit 1
fi
echo "[1/6] Python 3: $(python3 --version)"

# --- Step 2: Create venv ---
if [ ! -d "venv" ]; then
    echo "[2/6] Creating virtual environment..."
    python3 -m venv venv
else
    echo "[2/6] Virtual environment already exists."
fi

# --- Step 3: Install requirements ---
echo "[3/6] Installing Python dependencies..."
./venv/bin/pip install -q -r requirements.txt
echo "      Done."

# --- Step 4: Check PostgreSQL ---
if ! command -v psql &>/dev/null && ! command -v createdb &>/dev/null; then
    echo "[4/6] Warning: PostgreSQL (psql/createdb) not found."
    echo "      Install PostgreSQL, then create the database and run the migration manually."
    echo "      See README or docs/SETUP_SCRIPT_GUIDE.md."
else
    echo "[4/6] PostgreSQL found."

    # --- Step 5: Create database ---
    if createdb task_tracker 2>/dev/null; then
        echo "[5/6] Database 'task_tracker' created."
    else
        echo "[5/6] Database 'task_tracker' already exists or createdb failed (check permissions)."
    fi

    # --- Step 6: Run migration ---
    if [ -f "migrations/001_create_tasks_table.sql" ]; then
        echo "[6/6] Running migration..."
        if psql -d task_tracker -f migrations/001_create_tasks_table.sql &>/dev/null; then
            echo "      Migration applied."
        else
            echo "      Migration failed. Run manually: psql -d task_tracker -f migrations/001_create_tasks_table.sql"
        fi
    else
        echo "[6/6] Migration file not found; skipping."
    fi
fi

# --- Create .env from .env.example ---
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo ""
    echo "Created .env from .env.example."
    echo "  → Edit .env and set DB_USER and DB_PASSWORD to your PostgreSQL username and password."
else
    echo ""
    echo ".env already exists; not overwriting."
fi

echo ""
echo "=== Setup complete ==="
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo "  2. If you haven't already, edit .env with your DB_USER and DB_PASSWORD."
echo "  3. Run the app:"
echo "     python main.py"
echo ""
