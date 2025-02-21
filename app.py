##To-Do List Application

#To-Do List Application - 1

tasks = []

while True:
    print("Options:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)

    elif choice == "2":
        try:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            task_num = int(input("Enter the number of the task to remove: "))
            tasks.pop(task_num - 1)
        except (ValueError, IndexError):
            print("Invalid task number, try again")

    elif choice == "3":
        print("To-Do List:")
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("No tasks available")

    elif choice == "4":
        break

    else:
        print("Invalid choice, try again")