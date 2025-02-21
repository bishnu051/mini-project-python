from datetime import datetime


##To-Do List Application

#To-Do List Application - 1

tasks = []
priority_map = ("Low", "Medium", "High")

while True:
    print("Options:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        print("Task registered")

        while True:
            print("Enter priority for this task")
            print("1. Low")
            print("2. Medium")
            print("3. High")

            priority = input("Enter priority: ")

            try:
                priority = int(priority)
                if priority in (1, 2, 3):
                    break
                else:
                    print("Invalid choice, try again")
            except ValueError:
                print("Invalid input, please enter a number (1, 2, or 3)")

    elif choice == "2":
        try:
            for i, (task, priority, deadline) in enumerate(tasks, start=1):
                print(f"{i}. '{task}' - priority '{priority_map[priority-1]}' - deadline '{deadline}'")
            task_num = int(input("Enter the number of the task to remove: "))
            print(f"The task '{tasks[task_num-1][0]}' has been removed from the to do list")
            tasks.pop(task_num - 1)
        except (ValueError, IndexError):
            print("Invalid task number, try again")

    elif choice == "3":
        print("To-Do List:")
        if tasks:
            sorted_tasks = sorted(tasks, key=lambda x: (x[2], -x[1]))

            print("Good afternoon! Here are the tasks on the to-do-list:")

            for i, (task, priority, deadline) in enumerate(sorted_tasks, start=1):
                print(f"{i}. {task} - Priority: {priority_map[priority - 1]} - Deadline: {deadline}")
        else:
            print("No tasks available")

    elif choice == "4":
        if tasks == []:
            print("no tasks available")
        else:
            # sorting tasks based on date first and then priority
            sorted_tasks = sorted(tasks, key=lambda x: (x[2], -x[1]))
            top_tasks = sorted_tasks[:3]

            print("Good afternoon! Here are some tasks you might want to work on:")

            for i, (task, priority, deadline) in enumerate(top_tasks, start=1):
                print(f"{i}. {task} - Priority: {priority_map[priority-1]} - Deadline: {deadline}")

    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid choice, try again")
