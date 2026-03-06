-- Migration: create the tasks table
-- Run this once against your PostgreSQL database (see README or SQL_GUIDE.md).

-- Drop the table if it already exists (useful when re-running during development).
-- Remove this line when you use proper migrations (e.g. Alembic) in production.
DROP TABLE IF EXISTS tasks;

-- Create the tasks table.
-- SERIAL = auto-incrementing integer; PostgreSQL creates a sequence for it.
CREATE TABLE tasks (
    id          SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    status      VARCHAR(20) NOT NULL DEFAULT 'todo',
    urgency     VARCHAR(20) NOT NULL DEFAULT 'not_urgent',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT now(),

    -- Only allow these values for status and urgency.
    CONSTRAINT status_check  CHECK (status  IN ('todo', 'in_progress', 'done')),
    CONSTRAINT urgency_check CHECK (urgency IN ('urgently', 'medium_urgent', 'not_urgent'))
);

-- Optional: create an index so listing by status or urgency is faster when you have many rows.
CREATE INDEX idx_tasks_status  ON tasks (status);
CREATE INDEX idx_tasks_urgency ON tasks (urgency);
CREATE INDEX idx_tasks_created_at ON tasks (created_at DESC);

-- Optional: trigger to set updated_at automatically on every UPDATE.
-- You can add this later when you learn triggers, or update updated_at from your app.
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = now();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tasks_updated_at
    BEFORE UPDATE ON tasks
    FOR EACH ROW
    EXECUTE FUNCTION set_updated_at();
