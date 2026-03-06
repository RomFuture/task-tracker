Connecting / quitting
-Connect to DB (from shell):
--psql -d task_tracker
-Connect to another DB (inside psql):
--\c task_tracker
-Quit psql:
--\q

Seeing your tables and schema
-List all tables:
--\dt
-Describe one table (columns, types, constraints):
--\d tasks
-List all databases:
--\l
-List all roles/users:
--\du

Seeing your tasks (rows)
-All tasks:
--SELECT * FROM tasks;
-Only todo tasks:
--SELECT * FROM tasks WHERE status = 'todo';
-Only in_progress tasks:
--SELECT * FROM tasks WHERE status = 'in_progress';
-Only done tasks:
--SELECT * FROM tasks WHERE status = 'done';

Helpful extras
-Turn on “pretty” vertical display for wide rows:
--\x
-List available backslash commands:
--\?
-Help for a specific SQL command (e.g. SELECT):
--\h SELECT


UPDATE/CREATE THE requirements of a project
-pip install -r requirements.txt