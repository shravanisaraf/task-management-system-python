import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
import os

# Initialize NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description, priority, deadline):
        self.tasks.append({"description": task_description, "priority": priority, "deadline": deadline})

    def list_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['description']} (Priority: {task['priority']}, Deadline: {task['deadline']})")
        else:
            print("No tasks found.")

    def delete_task(self, task_number):
        try:
            del self.tasks[task_number - 1]
            print("Task deleted successfully!")
        except IndexError:
            print("Invalid task number. No task deleted.")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self, filename="tasks.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.tasks = json.load(file)
                print("Tasks loaded successfully.")
        else:
            print("No tasks found.")

def process_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())
    
    # Remove stop words and punctuation
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    
    # Intent recognition
    intent = recognize_intent(filtered_tokens)
    
    return intent

def recognize_intent(tokens):
    # Intent recognition using keyword matching
    if 'add' in tokens and 'task' in tokens:
        return 'ADD_TASK'
    elif 'list' in tokens and 'task' in tokens:
        return 'LIST_TASKS'
    elif 'delete' in tokens and 'task' in tokens:
        return 'DELETE_TASK'
    else:
        return 'UNKNOWN'

def main():
    task_manager = TaskManager()
    task_manager.load_tasks()  # Load tasks from file, if available
    print("Welcome to Task Manager!")

    while True:
        print("\nMain Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Finished (Delete Task)")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")
        
        if choice == '1':
            task_description = input("Enter task description: ")
            priority = input("Enter priority (High, Medium, Low): ").capitalize()
            while priority not in ["High", "Medium", "Low"]:
                print("Invalid priority. Please enter High, Medium, or Low.")
                priority = input("Enter priority (High, Medium, Low): ").capitalize()
            deadline = input("Enter deadline: ")
            task_manager.add_task(task_description, priority, deadline)
            print("Task added successfully!")
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            task_manager.list_tasks()
            task_number = int(input("Enter the number of the task you want to mark as finished: "))
            task_manager.delete_task(task_number)
        elif choice == '4':
            task_manager.save_tasks()  # Save tasks before exiting
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    print("Thank you for using Task Manager!")

if __name__ == "__main__":
    main()
