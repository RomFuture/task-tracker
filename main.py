import services.task_service as task_service
task_service = task_service.TaskService()


def _menu():
    """Print the main menu."""
    width = 52
    print()
    print("┌" + "─" * (width - 2) + "┐")
    print("│" + "  TASK TRACKER".center(width - 2) + "│")
    print("│" + "  Manage your tasks from the CLI".center(width - 2) + "│")
    print("└" + "─" * (width - 2) + "┘")
    print()
    print("  Commands")
    print("  " + "─" * (width - 4))
    print("  add <description>              Add a new task")
    print("  list                           Show all tasks")
    print("  list-status <status>           Filter by todo / in_progress / done")
    print("  update <id> <description>      Change task text")
    print("  delete <id>                    Remove a task")
    print("  mark-in-progress <id>          Set status to in progress")
    print("  mark-done <id>                 Set status to done")
    print("  exit                           Quit")
    print()


def main():
    error_message = None
    while True:
        print("\n" * 40)
        _menu()
        if error_message:
            print("  " + "─" * 48)
            print(f"  ⚠  {error_message}")
            print("  " + "─" * 48)
            error_message = None
        answer = input("  Enter a command: ").strip().lower()
        if answer == "exit":
            print("Exiting the program...")
            task_service.close_db_connection()
            break
        error_message = choice(answer)


def choice(command):
    """Run the command. Returns an error string to show on next menu, or None."""
    dict_commands = {
        "add": task_service.add_task,
        "list": task_service.list_tasks,
        "list-status": task_service.list_tasks_status,
        "update": task_service.update_task,
        "delete": task_service.delete_task,
        "mark-in-progress": task_service.mark_task_in_progress,
        "mark-done": task_service.mark_task_done
    }

    con_with_arg = command.split()
    con_with_arg = [item for item in con_with_arg]
    if not con_with_arg:
        return "No command provided."
    con_with_arg[0] = con_with_arg[0].lower()

    if con_with_arg[0] == "update":
        if len(con_with_arg) < 3:
            return "update needs: update <id> <new description>"
        err = dict_commands["update"](con_with_arg[1], " ".join(con_with_arg[2:]))
        return err
    elif con_with_arg[0] in dict_commands and len(con_with_arg) >= 2:
        if con_with_arg[0] == "add":
            err = dict_commands[con_with_arg[0]](" ".join(con_with_arg[1:]))
        else: err = dict_commands[con_with_arg[0]](con_with_arg[1])
        return err
    elif con_with_arg[0] == "list":
        err = dict_commands["list"]()
        return err
    elif len(con_with_arg) == 1:
        return "No argument provided. Please add it."
    else: return "Unknown command or wrong arguments."


if __name__ == "__main__":
    main()