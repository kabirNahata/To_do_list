tasks = []
FILE_NAME = 'To-Do-List.txt'

# Load existing tasks when starting the app
def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            loaded_tasks = f.read().splitlines()
            return [task for task in loaded_tasks if task.strip()]
    except FileNotFoundError:
        return []

# Shows menu 
def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save and Exit")

# Save tasks to file
def save_tasks(tasks_list):
    with open(FILE_NAME, "w") as f:
        for task in tasks_list:
            f.write(f"{task}\n")

# Load any existing tasks when starting
tasks = load_tasks()
    
while True:
    show_menu()
    try:
        choice = int(input("Enter your choice: ")) # Choice to choose between 4 options.
    except ValueError:
        print("Please enter a number.") # if the user enters something else than the optional number.
        continue

    if choice == 1: # Lets you view the task
        if len(tasks) == 0:
            print("You do not have any tasks currently!") # When you have no task in the list
        else:
            print("\nYour Tasks:") # When you have taks in the list
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
    
    elif choice == 2:
        new_task = input("\nEnter your task: ").strip()
        if new_task:
            tasks.append(new_task)
            print("Task added!")
        else:
            print("Task cannot be empty!")
                    
    elif choice == 3:
        if len(tasks) == 0:
            print("No tasks to delete!")
            continue

        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        
        try:
            remove = int(input("Choose a task number you want to delete: "))
            if 1 <= remove <= len(tasks):
                deleted_task = tasks.pop(remove-1)
                print(f"Deleted task: {deleted_task}")
                if len(tasks) == 0:
                    print("No tasks remaining!")
                else:
                    print("\nRemaining Tasks:")
                    for i, task in enumerate(tasks):
                        print(f"{i + 1}. {task}")
            else:
                print(f"Please enter a number between 1 and {len(tasks)}.")
        except ValueError:
            print("Please enter a valid number.")
                        
    elif choice == 4:
        save_tasks(tasks)
        print("Tasks saved!")
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")
      
        