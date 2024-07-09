import json
import os

TASK_FILE = 'tasks.json'


def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            tasks = json.load(f)
    return tasks


def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    new_task = {
        'title': title,
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks, TASK_FILE)
    print("Task added successfully!")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            status = 'Done' if task['completed'] else 'Not Done'
            print(f"{index}. {task['title']} - {task['description']} [{status}]")

def complete_task(tasks):
    list_tasks(tasks)
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks, TASK_FILE)
        print(f"Task '{tasks[task_index]['title']}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks(TASK_FILE)

    while True:
        print("\n==== To-Do List Menu ====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
