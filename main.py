from datetime import datetime
from tkinter import *

window = Tk()
window.title("To-Do List")
window.geometry("500x700")

# Function to add task
def add_task():
    task = task_entry.get()

    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
        save_tasks()

# Function to delete selected task

def complete_task():
    selected = task_listbox.curselection()

    if selected:
        task = task_listbox.get(selected)
        task_listbox.delete(selected)
        task_listbox.insert(selected, "✔ " + task)
        save_tasks()
        
def delete_task():
    selected = task_listbox.curselection()

    if selected:
        task_listbox.delete(selected)
        save_tasks()
        
# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, END)
    save_tasks()

# Save tasks to file
def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        tasks = task_listbox.get(0, END)
        for task in tasks:
            file.write(task + "\n")

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for task in file:
                task_listbox.insert(END, task.strip())
    except FileNotFoundError:
        pass

# Task count
def update_count():
    count_label.config(text = f'Total Tasks: {task_listbox.size()}')

# Title
title = Label(window, text="My To-Do List", font=("Segoe UI", 18, "bold"))
title.pack(pady=10)

# Date and Time
time_label = Label(window, text = datetime.now().strftime('%d-%m-%Y  %I:%M %p'), font=("Segoe UI", 10), bg = 'lightblue')
time_label.pack()

# Entry box
task_entry = Entry(window, width=30, font=("Segoe UI", 14))
task_entry.pack(pady=10)

# Add button
add_button = Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Task list
task_listbox = Listbox(window, width=35, height=12, font=("Segoe UI", 12))
task_listbox.pack(pady=10)

#task count
count_label = Label(window, text='Total Taks: 0', font=('Segoe UI', 10), bg = 'lightblue')
count_label.pack()

# Delete button
complete_button = Button(window, text="✔ Complete", command=complete_task)
complete_button.pack(pady=5)

delete_button = Button(window, text="🗑 Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Clear All button
clear_button = Button(window, text="Clear All", command=clear_tasks)
clear_button.pack(pady=5)

load_tasks()
update_count()

window.mainloop()