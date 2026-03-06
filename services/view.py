"""
Format and display task data for the CLI.
Expects rows as (id, description, status, urgency, created_at, updated_at).
"""


def _short_date(ts):
    """Turn a timestamp into a short string for display."""
    if ts is None:
        return "—"
    s = str(ts)
    return s[:19] if len(s) >= 19 else s


def format_and_print_tasks(rows):
    """
    Print a list of task rows in a readable card-style format.
    Each row: (id, description, status, urgency, created_at, updated_at).
    """
    if not rows:
        print("No tasks found.")
        return
    for row in rows:
        task_id, description, status, urgency, created_at, updated_at = (
            row[0], row[1], row[2], row[3], row[4], row[5]
        )
        print("-" * 50)
        print(f"  [{task_id}]  {description}")
        print(f"  Status  : {status}")
        print(f"  Urgency : {urgency}")
        print(f"  Created : {_short_date(created_at)}")
        print(f"  Updated : {_short_date(updated_at)}")
    print("-" * 50)
