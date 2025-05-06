import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
STATUS_OPTIONS = {"todo", "in-progress", "done"}


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def generate_task_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1


def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_task_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")


def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print("Task updated successfully")
            return
    print("Task not found")


def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task deleted successfully")


def mark_task(task_id, status):
    if status not in STATUS_OPTIONS:
        print("Invalid status")
        return
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task marked as {status}")
            return
    print("Task not found")


def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if status is None or task["status"] == status]
    for task in filtered_tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Updated: {task['updatedAt']})")


def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        return
    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(sys.argv[2])
    elif command == "update" and len(sys.argv) >= 4:
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete" and len(sys.argv) >= 3:
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) >= 3:
        mark_task(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) >= 3:
        mark_task(int(sys.argv[2]), "done")
    elif command == "list":
        status = sys.argv[2] if len(sys.argv) >= 3 else None
        if status and status not in STATUS_OPTIONS:
            print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
        else:
            list_tasks(status)
    else:
        print("Invalid command or missing arguments")


if __name__ == "__main__":
    main()
