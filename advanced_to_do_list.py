# TO DO LIST 2.
import json
from datetime import datetime

#function to convert string to python readable date format
def date_conversion(date): return datetime.strptime(date, "%Y-%m-%d").date()

#dummy  list for debugging
to_do_list = [
    {"description": "Submit report", "priority": "Medium", "deadline": date_conversion("2025-05-05")},
    {"description": "Doctor appointment", "priority": "High", "deadline": date_conversion("2025-05-08")},
    {"description": "Grocery shopping", "priority": "Low", "deadline": date_conversion("2025-03-05")},
    {"description": "Grocery shopping 2", "priority": "High", "deadline": date_conversion("2025-03-05")},
    {"description": "Finish assignment", "priority": "High", "deadline": date_conversion("2025-03-08")}
]

#list for completed tasks
completed_tasks = []

#function for sorting tasks based on deadline first and then by priority
def sort_tasks():
    return sorted(
        to_do_list,
        key=lambda x: (x["deadline"], -priority_map.index(x["priority"]))
    )

#priority mapping from integer to string for display
priority_map = ("Low", "Medium", "High")

#function to save list as json file
def save_to_file(filename="todo_list.json"):
    sorted_tasks = sort_tasks()

    with open(filename, "w") as file:
        json.dump(sorted_tasks, file, default=str, indent=4)  # Convert dates to strings
    print("To-Do List saved as json successfully!")

#priority handling function, returns priority string based on integer input
def add_priority():
    while True:
        print("Enter priority for this task:")
        print("1. Low")
        print("2. Medium")
        print("3. High")

        priority = input("Enter priority (1, 2, or 3) or '0' to cancel: ")
        if priority == "0":
            print("Add task cancelled.")
            return priority

        try:
            priority = int(priority)
            if priority in (1, 2, 3):
                return priority_map[priority - 1]
            else:
                print("Invalid choice, please enter (1, 2, or 3) or '0' to cancel .")
        except ValueError:
            print("Invalid input, please enter a number.")

#deadline handling function
def get_deadline():
    while True:
        print("Enter deadline for this task")

        deadline = input("Enter deadline (YYYY-MM-DD) or '0'  to cancel: ")
        if deadline == "0":
            print("Add task cancelled.")
            return deadline

        try:
            deadline_date = date_conversion(deadline)
            print(deadline_date)
            today_date = datetime.today().date()

            #checks if the deadline date is in the future or not
            if deadline_date > today_date:
               return deadline_date
            else:
                print("Invalid choice: Deadline must be in the future. Try again.")
        except ValueError:
            print("Invalid input: Please enter the date in YYYY-MM-DD format or '0' to cancel.")


def add_task():
    task = input("Enter the task name or '0' to cancel: ")
    if task == "0":
        print("Add task cancelled.")
        return

    print("Task registered")

    priority = add_priority()
    if priority == "0":
        return
    deadline = get_deadline()
    if deadline == "0":
        return

    to_do_list.append({
        "description": task,
        "priority": priority,
        "deadline": deadline
    })

    print(f"'{task}' with priority '{priority}' and deadline '{deadline}' has been added to the list.")


def view_tasks():
    if not to_do_list:
        print("To-Do List is empty")
        return

    print("Here are the tasks in the to-do-list")
    sorted_tasks = sort_tasks()
    for count, task in enumerate(sorted_tasks, start=1):
        print(f"{count}. {task['description']} - {task['priority']} - {task['deadline']}")

def view_completed_tasks():
    if not completed_tasks:
        return
    print("Completed Tasks")
    for count, task in enumerate(completed_tasks, start=1):
        print(f"{count}. {task['description']} - {task['priority']} - {task['deadline']}")


def remove_task():
    for count, task in enumerate(to_do_list, start=1):
        print(f"{count}. {task['description']} - {task['priority']} - {task['deadline']}")

    while True:
        task_to_remove = input("Enter the task number to remove or '0' to cancel: ")

        if task_to_remove == '0':
            print("Task removal cancelled.")
            return

        task_to_remove = int(task_to_remove)
        try:
            if 1 <= task_to_remove <= len(to_do_list):
                removed_task = to_do_list.pop(task_to_remove - 1)
                print(f"'{removed_task['description']}' has been removed from the list.")
                return
            else:
                print("Invalid choice: Please enter a valid task number.")

        except ValueError:
            print("Invalid input: Please enter the task number (1 to )")


def suggest_task():
    if not to_do_list:
        print("No tasks available to suggest.")
        return

    sorted_tasks = sort_tasks()

    print("\nHere are some suggested tasks based on deadline and priority:")
    for i, task in enumerate(sorted_tasks[:3], start=1):
        print(f"{i}. {task['description']} - {task['priority']}, - {task['deadline']}")

def mark_task_as_complete():
    for count, task in enumerate(to_do_list, start=1):
        print(f"{count}. {task['description']} - {task['priority']} - {task['deadline']}")

    while True:
        task_to_complete = input("Enter the task number to mark completed or '0' to cancel.")
        if task_to_complete == '0':
            print("Task completion cancelled.")
            return

        task_to_complete = int(task_to_complete)
        try:
            if 1 <= task_to_complete <= len(to_do_list):
                completed_tasks.append(to_do_list[task_to_complete - 1])
                removed_task = to_do_list.pop(task_to_complete - 1)
                print(f"'{removed_task['description']}' has been marked completed.")
                return
            else:
                print("Invalid choice: Please enter a valid task number.")

        except ValueError:
            print("Invalid input: Please enter the task number (1 to )")

def clear_completed_tasks():
    if not completed_tasks:
        print("Completed tasks list empty")
        return
    completed_tasks.clear()
    print("Completed tasks cleared")

# Main function to drive the program
def main():
    while True:
        print()
        print("Advanced To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Suggest Task")
        print("5. Mark Task as complete")
        print("6. Clear completed tasks")
        print("7. Save list as a file")
        print("8. Exit")


        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
            view_completed_tasks()
        elif choice == '4':
            suggest_task()
        elif choice == '5':
            mark_task_as_complete()
        elif choice == '6':
            clear_completed_tasks()
        elif choice == '7':
            save_to_file()
        elif choice == '8':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 5.")


# Run the main function to start the program
main()
