import json
import os

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def to_dict(self):
        return {'title': self.title, 'completed': self.completed}

    @staticmethod
    def from_dict(data):
        task = Task(data['title'])
        task.completed = data['completed']
        return task

class ToDoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Task.from_dict(task) for task in data]
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
        print(f"✅ Task added: {title}")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
        for i, task in enumerate(self.tasks, 1):
            status = "✔️" if task.completed else "❌"
            print(f"{i}. {task.title} [{status}]")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print("✅ Task marked as completed.")
        else:
            print("❌ Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑️ Task deleted: {removed.title}")
        else:
            print("❌ Invalid task number.")

def menu():
    todo = ToDoList()
    while True:
        print("\n📋 TO-DO LIST MENU")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            todo.view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            todo.add_task(title)
        elif choice == '3':
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo.delete_task(index)
        elif choice == '5':
            print("👋 Exiting...")
            break
        else:
            print("⚠️ Invalid input, try again.")

if __name__ == "__main__":
    menu()
