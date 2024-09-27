# codesoft
CodesoftHub ,CodeSoftly, SoftCodes, CodeSoftLab ,SoftCraft, SoftCodeBase
def main():
    tasks = []
    while True:
        print("\n=====To-DO-List=====")
        print("1. Add Task")
        print("2. Show All Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Show Pending Tasks")
        print("6. Exit")
        
        choice = input("Enter Your choice: ")
        
        if choice == '1':  # Add Task
            n_tasks = int(input("How many tasks you want to add: "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                priority = input("Enter the priority (low, medium, high): ").lower()
                tasks.append({"task": task, "done": False, "priority": priority})
            print("Task(s) added!")
        
        elif choice == '2':  # Show All Tasks
            print("\nAll Tasks:")
            if tasks:
                for index, task in enumerate(tasks):
                    status = "Done" if task["done"] else "Not Done"
                    print(f"{index + 1}. {task['task']} - {status} - Priority: {task['priority']}")
            else:
                print("No tasks to show.")
        
        elif choice == '3':  # Mark Task as Done
            task_index = int(input("Enter the task number to mark done: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")
        
        elif choice == '4':  # Remove Task
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Removed task: {removed_task['task']}")
            else:
                print("Invalid task number.")
        
        elif choice == '5':  # Show Pending Tasks
            print("\nPending Tasks:")
            pending_tasks = [task for task in tasks if not task["done"]]
            if pending_tasks:
                for index, task in enumerate(pending_tasks):
                    print(f"{index + 1}. {task['task']} - Not Done - Priority: {task['priority']}")
            else:
                print("No pending tasks!")
        
        elif choice == '6':  # Exit
            print("Exiting the To-Do List.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
