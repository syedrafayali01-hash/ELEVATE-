
import os
FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME,'r') as file:
        return [line.strip() for line in file.readlines()]
    
def save_tasks(tasks):
    with open(FILE_NAME,'w') as file:
        for task in tasks:
            file.write(task + "\n")
            
def show_menu():
    print("\n====== TO-DO LIST MENU =======")
    print("1. Veiw Tasks")
    print("2. Add Tasks")
    print("3. Remove Tasks")
    print("4. EXIT")
    
def view_tasks(tasks):
    if not tasks:
        print("Tasks not found. ")
    else:
        print("\n Your Tasks.")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        
def add_task(tasks):
        task = input ("enter new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added sucessfully!")
        
def remove_tasks(tasks):
        view_tasks(tasks)
        try:
            index = int(input("Enter task number to remove: "))
            if 1 <= index <= len(tasks):
                removed = tasks.pop(index - 1)
                save_tasks(tasks)
                print(f"Task '{removed}' removed sucessfully!")
            else:
                print("Invalid task number. ")
        except ValueError:
            print("Please enter a valid number. ")
            
            
def main():
        tasks = load_tasks()
        
        while True:
            show_menu()
            choice = input("Enter your choice (1-4): ")
            
            if choice == "1":
                view_tasks(tasks)
            elif choice == "2":
                add_task(tasks)
            elif choice == "3":
                remove_tasks(tasks)
            elif choice == "4":
                print("Exiting TO-DO App. Goodbye! ")
                break
            else:
                print("Invalid choice! Please select 1-4. ")
                
if __name__ == "__main__":
    main()
    
            
            
            