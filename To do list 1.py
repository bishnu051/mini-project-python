to_do_list = [] # Empty list

# Add Task
def add_task(tasks):
    task = input("Enter the task:")
    tasks.append(task)
    print(f"{task} has been added to the list")

# Remove Task
def remove_task(tasks):
    task = input("Enter the task to remove:")
    if task in tasks:
        tasks.remove(task)
        print(f"{task} has been removed from the list")
    else:
        print("Task not found in list")

# View Tasks
def view_tasks(tasks):
    if tasks:
        print("To-Do List: ")
        for count, task in enumerate(tasks, start = 1):
            print(count, task)
    else:
        print("To-Do List is empty")

# Menu
def menu ():
    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice =  input("Enter your choice:")

        if choice == "1":
            add_task(to_do_list)
        elif choice == "2":
            remove_task(to_do_list)
        elif choice == "3":
            view_tasks(to_do_list)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")
        print()

if __name__ == "__main__":
    menu()