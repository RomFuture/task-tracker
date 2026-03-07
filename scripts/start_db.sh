#!/usr/bin/env bash
# Start PostgreSQL (Debian) and open psql on task_tracker database.
# Run from project root: ./scripts/start_db.sh

set -e

echo "Starting PostgreSQL..."
sudo systemctl start postgresql

echo "Opening psql (database: task_tracker)..."
psql -d task_tracker
