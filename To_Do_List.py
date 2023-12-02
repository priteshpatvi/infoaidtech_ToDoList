import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Status: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                self.tasks.remove(task)
                return True
        return False

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def save_tasks(self, filename):
        task_data = [{'title': task.title, 'description': task.description, 'status': task.status} for task in self.tasks]
        with open(filename, 'w') as file:
            json.dump(task_data, file)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                task_data = json.load(file)
                self.tasks = [Task(**data) for data in task_data]
        except FileNotFoundError:
            print("File not found. No tasks loaded.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            todo_list.add_task(task)
        elif choice == "2":
            task_title = input("Enter task title to delete: ")
            if todo_list.delete_task(task_title):
                print(f"{task_title} has been deleted.")
            else:
                print(f"Task '{task_title}' not found.")
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
            print("Tasks saved to file.")
        elif choice == "5":
            filename = input("Enter filename to load tasks from: ")
            todo_list.load_tasks(filename)
            print("Tasks loaded from file.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
