# ============================================================
# FILE: day_7.py
# TOPIC: File I/O, match-case, dictionaries, CRUD operations
# FOLDER: challenges/01_utilities
# CHALLENGE DAY: Day 7
# ============================================================
# Yeh challenge sikhata hai:
# - CRUD = Create, Read, Update, Delete (task manager mein sab kuch)
# - File se data load/save karna (persistence = program band hone ke baad bhi data rahe)
# - Dictionary list = har task ek dict hai {"text": ..., "done": ...}
# - match-case statement (Python 3.10+) = switch-case jaisa
# - enumerate() = index + item dono milta hai loop mein
# - os.path.exists() = file hai ya nahi check karo
# ============================================================

"""
 Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting
"""

import os

# Constant = file ka naam ek jagah define karo (baad mein change karna easy)
TASK_FILE = "tasks.txt"

# File se saari tasks load karo aur list of dictionaries return karo
def load_tasks():
    tasks = []
    # os.path.exists = file maujood hai ya nahi check karo
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                # rsplit("||", 1) = RIGHT se sirf 1 baar split karo
                # Kyunki task text mein bhi "||" ho sakta hai
                text, status = line.strip().rsplit("||", 1)
                # Dictionary banake list mein add karo
                tasks.append({"text": text, "done": status == "done"})
    return tasks

# Saari tasks ko file mein save karo (overwrite mode "w")
def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")

# Tasks ko numbered list ki tarah screen par dikhao
def display_tasks(tasks):
    if not tasks:
        print(f"NO tasks found")
    else:
        # enumerate(tasks, 1) = 1 se numbering start (0 nahi)
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

# Main task manager function - menu driven program
def task_manager():
    tasks = load_tasks()  # program start par file se tasks load karo

    while True:  # menu loop - tab tak chalega jab tak user exit na kare
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()

        # match-case = choice ke hisaab se alag action (switch-case jaisa)
        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text":text, "done": False})
                    save_tasks(tasks)  # har change ke baad file update karo
                else:
                    print("Task cannot be empty")

            case "2":
                display_tasks(tasks)
            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number"))
                    # 1 <= num <= len(tasks) = valid range check
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True  # list index 0 se start, user 1 se
                        save_tasks(tasks)
                        print("task marked as DONE")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "4":
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number to delete"))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1)  # pop = item hatao aur return karo
                        save_tasks(tasks)
                        print(f"task removed {removed['text']}")
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Please enter a number")
            case "5":
                print("Exiting task Manager")
                break
            case _:
                # _ = default case - koi bhi invalid option
                print("Please choose a valid option")

task_manager()
