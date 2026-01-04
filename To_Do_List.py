def to_do_list():
    tasks = []

    while True:
        print("1. Add task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f'Task "{task}" added.')
        elif choice == '2':
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
            else:
                print(f'Task "{task}" not found.')
        elif choice == '3':
            if tasks:
                print("Your tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks in the list.")
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

to_do_list()