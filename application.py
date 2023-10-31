import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class TodoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date):
        task = Task(description, due_date)
        self.tasks.append(task)


    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            task.completed = True
            self.completed_tasks.append(task)
        else:
            messagebox.showerror("Error", "Invalid task index")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
        else:
            messagebox.showerror("Error", "Invalid task index")

def add_task_clicked():
    description = description_entry.get()
    due_date = due_date_entry.get()
    todo_list.add_task(description, due_date)
    update_task_list()
    clear_entry_fields()  # Clear the entry fields after adding a task

def mark_task_completed():
    task_index = int(selected_task.get())
    todo_list.mark_task_completed(task_index)
    update_task_list()

def remove_task():
    task_index = int(selected_task.get())
    if 1 <= task_index <= len(todo_list.tasks):
        todo_list.remove_task(task_index)
        update_task_list()
    else:
        messagebox.showerror("Error", "Invalid task index")


def clear_entry_fields():
    description_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)

def update_task_list():
    task_listbox.delete(0, tk.END)
    
    for index, task in enumerate(todo_list.tasks, start=1):
        status = "Not Completed"
        task_listbox.insert(tk.END, f"{index}. Description: {task.description} | Due Date: {task.due_date} | Status: {status}")

    task_listbox.insert(tk.END, '')  # Add a separator between active and completed tasks

    for index, task in enumerate(todo_list.completed_tasks, start=1):
        status = "Completed"
        task_listbox.insert(tk.END, f"{index}. Description: {task.description} | Due Date: {task.due_date} | Status: {status}")

root = tk.Tk()
root.title("To-Do List Application")

# Create a TodoList instance
todo_list = TodoList()

# Entry fields for adding tasks
description_label = tk.Label(root, text="Description:", font=("Helvetica", 12))
description_label.pack()
description_entry = tk.Entry(root, font=("Helvetica", 12))
description_entry.pack()

due_date_label = tk.Label(root, text="Due Date:", font=("Helvetica", 12))
due_date_label.pack()
due_date_entry = tk.Entry(root, font=("Helvetica", 12))
due_date_entry.pack()



add_task_button = tk.Button(root, text="Add Task", command=add_task_clicked, font=("Helvetica", 12), bg="green", fg="white")
add_task_button.pack()

# List of tasks
task_list_label = tk.Label(root, text="Task List", font=("Helvetica", 14, "bold"))
task_list_label.pack()

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, font=("Helvetica", 12))
task_listbox.pack()

# Mark as completed and Remove buttons
selected_task_label = tk.Label(root, text="Select Task:", font=("Helvetica", 12))
selected_task_label.pack()

selected_task = tk.StringVar()
selected_task_entry = tk.Entry(root, textvariable=selected_task, font=("Helvetica", 12))
selected_task_entry.pack()

mark_completed_button = tk.Button(root, text="Mark as Completed", command=mark_task_completed, font=("Helvetica", 12), bg="blue", fg="white")
mark_completed_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=("Helvetica", 12), bg="red", fg="white")
remove_button.pack()

# Start the main GUI loop
update_task_list()
root.mainloop()
