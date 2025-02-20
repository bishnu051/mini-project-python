print("apple")
# TO DO LIST 2.
to_do_list = [] # Empty List

def add_task():
    task = input("Enter the task: ")
    priority = input("Enter the priority (high, medium, low): ")
    while priority not in ["high", "medium", "low"]:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        priority = input("Enter the priority (high, medium, low): ")
    deadline = input(" Enter the deadline (YYYY-MM-DD): ")

    to_do_list.append({
        "description": task,
        "priority": priority,
        "deadline": deadline
    })

    print(f"{task} with priority {priority} and deadline {deadline} has been added to the list.")

def remove_task():
    task_to_remove = input("Enter the task to remove: ")

    for task in to_do_list:
        if task["description"] == task_to_remove:
            to_do_list.remove(task)
            print(f"{task_to_remove} has been remove from the list.")
            break
    else:
        print(f"{task_to_remove} not found on the list")

def view_tasks():
    for count, task in enumerate(to_do_list, start=1):
        print(f"{count}. {task['description']} - {task['priority']} - {task['deadline']}")
    else:
        print("To-Do List is empty")

def suggest_task():
    sort_task = sorted(to_do_list, key = lambda x: (x["priority"] == "high", x['priority'] == 'medium', x['priority'] == 'low'), reverse=True)
    print("Here are some tasks you might want to work on:")
    for task in sort_task:
        print(f"{task['description']} - {task['priority']} - {task['deadline']}")

# Main function to drive the program
def main():
    while True:
        print("Advanced To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Suggest Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            suggest_task()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please select a number between 1 and 5.")
        print()

# Run the main function to start the program
if __name__ == "__main__":
    main()