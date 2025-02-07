
to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def view_tasks():
    if not to_do_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

def complete_task(index):
    if 1 <= index <= len(to_do_list):
        completed_task = to_do_list.pop(index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")


while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        index = int(input("Enter the task index to mark as completed: "))
        complete_task(index)
    elif choice == "4":
        print("Exiting the To-Do List program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
