import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    # Load tasks from file if it exists
    if os.path.exists(TODO_FILE):
        try:
            with open(TODO_FILE, 'r') as file:
                return json.load(file)
        except:
            return []
    return []

def save_tasks(tasks):
    # Save tasks to file
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

def display_menu():
    # Display the main menu
    print("="*30)
    print("LIGHTNING MCQUEEN'S TO-DO LIST")
    print("="*30)
    print("Gotta get ready for the big race!")
    print("Here's what's on deck:")
    print("-"*30)
    print("1. Add a task")
    print("2. View my to-do list")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Quit")
    print("-"*30)

def add_task(tasks):
    # Add a new task to the list
    task = input("What's the task, champ? ")
    tasks.append({"name": task, "done": False})
    save_tasks(tasks)
    print(f"\n✅ '{task}' has been added to your list!")

def view_tasks(tasks):
    # Display all tasks with their status
    if not tasks:
        print("\nYour to-do list is empty!")
        return
    
    print("\n" + "="*30)
    print("YOUR TO-DO LIST")
    print("="*30)
    
    for i, task in enumerate(tasks, 1):
        status = "✅ DONE" if task["done"] else "⏳ PENDING"
        print(f"{i}. {task['name']} - {status}")
    
    print("\n")

def mark_done(tasks):
    # Mark a task as done
    if not tasks:
        print("Your to-do list is empty. No tasks to complete!")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Which task number did you finish? "))
        if 1 <= choice <= len(tasks):
            tasks[choice-1]["done"] = True
            save_tasks(tasks)
            print(f"✅ '{tasks[choice-1]['name']}' is checked off!")
        else:
            print("Invalid task number!")
            print("Enter a number: ")
    except ValueError:
        print("Invalid task number!")
        print("Enter a number: ")

def remove_task(tasks):
    # Remove a task from the list
    if not tasks:
        print("Your to-do list is empty. No tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        choice = int(input("Which task should we remove? "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice-1)
            save_tasks(tasks)
            print(f"🗑️'{removed['name']}' has been removed from the list!")
        else:
            print("Invalid task number!")
            print("Enter a number: ")
    except ValueError:
        print("Invalid task number!")
        print("Enter a number: ")

def main():
    tasks = load_tasks()    
    while True:
        display_menu()
        choice = input("What's the move, champ? ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Exiting Program..")
            break
        else:
            print("Invalid option!")
            print("Enter a number: ")