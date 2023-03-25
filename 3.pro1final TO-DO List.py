to_do_list = []

def add_task():
    task = input("Enter a task: ")
    to_do_list.append({"task": task, "completed": False})
    print("Task added successfully!\n\n")


def view_task():
    print("\n My To-Do List:")
    for index, task in enumerate(to_do_list):
        status = "Completed" if task["completed"] else "Incomplete"
        print(f"{index + 1}. {task['task']} - {status}\n")

def mark_task_completed():
    view_task()
    task_index = int(input("enter task number to mark as completed: ")) - 1
    to_do_list[task_index]["completed"] = True
    print("task marked as completed!\n")

def remove_completed_task():
    global to_do_list
    to_do_list = [task for task in to_do_list if not task["completed"]]
    print("Completed tasks removed successfully!\n")

while True:
    print("Welcome to To-Do List Application")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task as Completed")
    print("4. Remove Completed Task")
    print("5. Quit")

    choice = int(input("Enter your choice: \n"))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        mark_task_completed()
    elif choice == 4:
        remove_completed_task()
    elif choice == 5:
        print("Thank you for using To-Do List , Have a good day!!")
        break
    else:
        print("\n Invalid choice. Please try again.\n")
