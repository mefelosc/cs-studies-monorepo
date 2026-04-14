import json
import os
import sys

# File where tasks will be stored
TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Task {index} marked as done.")
    else:
        print("Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    else:
        print("Invalid task number.")

def show_help():
    print("Simple Task Manager")
    print("Usage:")
    print("  python simple_task_manager.py add <description>  - Add a new task")
    print("  python simple_task_manager.py list               - List all tasks")
    print("  python simple_task_manager.py done <number>       - Mark a task as done")
    print("  python simple_task_manager.py delete <number>     - Delete a task")

def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) > 2:
        try:
            complete_task(int(sys.argv[2]))
        except ValueError:
            print("Please provide a valid task number.")
    elif command == "delete" and len(sys.argv) > 2:
        try:
            delete_task(int(sys.argv[2]))
        except ValueError:
            print("Please provide a valid task number.")
    else:
        show_help()

if __name__ == "__main__":
    main()
