# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:05:20 2025

@author: Josh
"""
def add_task(tasks):
    task = input("What task would you like to add?")
    tasks.append(task)
    print("Task added.")
    
def view_tasks(tasks):
    print("Tasks:")
    for i, task in enumerate(tasks):
         print(i+1,{task})

def complete_task(tasks):
    view_tasks(tasks)
    comp_task = int(input("Enter the number of the task to complete:")) - 1
    del tasks[comp_task]
    print("Task completed.")
    
def delete_task(tasks):
    view_tasks(tasks)
    del_task = int(input("Enter the number of the task to delete:"))
    del tasks[del_task]
    print("Task deleted.")
    
def main():
    tasks = []
    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
main()