```python
# to_do_list.py

"""A simple to-do list application."""

import json
import os

DEFAULT_DATA_FILE = "todo_data.json"


def load_tasks(filepath=DEFAULT_DATA_FILE):
    """Loads tasks from a JSON file. Creates an empty list if the file doesn't exist."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON data in the file.  Creating a new file.")
        return []


def save_tasks(tasks, filepath=DEFAULT_DATA_FILE):
    """Saves tasks to a JSON file."""
    try:
        with open(filepath, "w") as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")


def add_task(tasks):
    """Adds a new task to the to-do list."""
    description = input("Enter task description: ")
    if not description:
        print("Task description cannot be empty.")
        return tasks
    tasks.append({"description": description, "completed": False})
    return tasks


def view_tasks(tasks):
    """Displays the to-do list."""
    if not tasks:
        print("No tasks in the list.")
        return

    print("\n--- To-Do List ---")
    for i, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{i+1}. {status} {task['description']}")
    print("---")


def mark_complete(tasks):
    """Marks a task as complete."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return tasks


def remove_task(tasks):
    """Removes a task from the to-do list."""
    view_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            del tasks[index]
            print("Task removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return tasks


def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Remove task")
        print("5. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tasks = add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            tasks = mark_complete(tasks)
        elif choice == "4":
            tasks = remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

```