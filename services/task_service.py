import services.db as db
import services.view as view


class TaskService:
    def __init__(self):
        self.db = db.DBConnection()
        self.conn, self.cursor = self.db.connect_to_db()
        self.ids = self.id_exicution()
    def id_exicution(self):
        self.cursor.execute("SELECT id FROM tasks")
        self.ids = [int(row[0]) for row in self.cursor.fetchall()]
        return self.ids
    def add_task(self, description):
        task = {
        "description": description,
        "status": "todo",
        "urgency": "urgently"
        }
        self.cursor.execute("INSERT INTO tasks (description, status, urgency) VALUES (%s, %s, %s) RETURNING id", (task["description"], task["status"], task["urgency"]))
        new_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.ids = self.id_exicution()
        print("\n" + f"\nTask added with id: {new_id}")
        input("Press Any Key to continue...")
        
    def list_tasks(self):
        self.cursor.execute("SELECT * FROM tasks ORDER BY id")
        tasks = self.cursor.fetchall()
        print("\n"*2)
        view.format_and_print_tasks(tasks)
        input("\nPress Any Key to continue...")
    
    def list_tasks_status(self, status):
        self.cursor.execute("SELECT * FROM tasks WHERE status = %s ORDER BY id", (status,))
        tasks = self.cursor.fetchall()
        print("\n" * 2)
        view.format_and_print_tasks(tasks)
        input("\nPress Any Key to continue...")
    
    def update_task(self, id, new_description):
        if int(id) not in self.ids:
            return "Task not found."
        self.cursor.execute("UPDATE tasks SET description = %s WHERE id = %s", (new_description, id))
        self.conn.commit()
        print("\n" + "Task updated successfully.")
        input("Press Any Key to continue...")
        return None

    def delete_task(self, id):
        if int(id) not in self.ids:
            return "Task not found."
        self.cursor.execute("DELETE FROM tasks WHERE id = %s RETURNING id", (id,))
        deleted_id = self.cursor.fetchone()[0]
        self.conn.commit()
        self.ids = self.id_exicution()
        print("\n" + f"Task deleted with id: {deleted_id}")
        input("Press Any Key to continue...")
        return None

    def mark_task_in_progress(self, id):
        if int(id) not in self.ids:
            return "Task not found."
        self.cursor.execute("UPDATE tasks SET status = 'in_progress' WHERE id = %s RETURNING id", (id,))
        self.conn.commit()
        print("\n" + f"Task marked as in progress with id: {id}")
        input("Press Any Key to continue...")
        return None

    def mark_task_done(self, id):
        if int(id) not in self.ids:
            return "Task not found."
        self.cursor.execute("UPDATE tasks SET status = 'done' WHERE id = %s RETURNING id", (id,))
        self.conn.commit()
        print("\n" + f"Task marked as done with id: {id}")
        input("Press Any Key to continue...")
        return None
    
    def close_db_connection(self):
        print("Closing database connection...")
        self.db.close_db_connection(self.cursor, self.conn)