class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")
        
    def edit_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task
            print("Task edited successfully.")
        else:
            print("INvalid task Index")
            
    def deleted_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted Successfully")
        else:
            print("Invalid task index.")
        
    def list_task(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

def main():
    todo_list = ToDoList()
    
    while True:
        print("/nTo-Do List Application")
        print("1. Add a Task")
        print("2. Edit a Task")
        print("3. Delete a Task")
        print("4. List all Task")
        print("Exit")
        
        choice = input("Enter your choice: ")
        
        if choice.lower() == "1" or choice.lower() == "add":
            task = input("Enter the task description.")
            todo_list.add_task(task)
        
        elif choice.lower() == "2" or choice.lower() == "edit":
            index = int(input("Enter the task index to edit:"))
            new_task = input("Enter the new task description:")
            todo_list.edit_task(index, new_task)
        
        elif choice.lower() == "3" or choice.lower() == "delete":
            index = int(input("Enter the task index to delete: "))
            todo_list.deleted_task(index)
        
        elif choice.lower() == "4" or choice.lower() == "list":
            todo_list.list_task()
        
        elif choice.lower() == "5" or choice.lower() == "exit":
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. PLease enter a number between 1 and 5.")

if __name__ == "__main__":
    main()