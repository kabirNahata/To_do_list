tasks = []

def show_menu():
    print("\n--- To-Do List App ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save and Exit")

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(tasks) == 0:
            print("You do not have any tasks currently!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
    
    elif choice == 2:
        new_task = str(input("\nEnter your task: "))
        tasks.append(new_task)
        print("Task added!")
    
    elif choice == 3:
        # for i in range(len(tasks)):
        #     print(tasks[i])
        remove = int(input("Choose a task no you want to delete? "))
        # print(remove)
        # deleted = tasks[remove]
        del tasks[remove-1]
        if len(tasks) == 0:
            print("No tasks remaining!")
        else:
            for i in range(len(tasks)):
                print(f"{i}:{tasks[i]}")

    elif choice == 4:
        print("Saved")
        print("Goodbye!")
        break

    else:
        print("That was not the correct option.")

            
        