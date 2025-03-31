import os
tasks=[]
def clear_screen():
    os.system('clear' if os.name=='posix' else 'cls')
def show_menu():
    clear_screen()
    print("To-Do List Task")
    print("1.Add Tasks")
    print("2.View Tasks")
    print("3.Mark as completed")
    print("4.Delete task")
    print("5.Exit")
def add_task():
    task=input("Enter a new task: ")
    tasks.append({"task":task,"completed":False})
    input("Task added.Press enter to continue...")
def view_tasks():
    clear_screen()
    print("To-Do List:")
    for i,task in enumerate(tasks,start=1):
        status="Done" if task["completed"] else "Not done"
        print(f"{i}.{task['task']}-Status:{status}")
    input("Press enter to continue...")  
def mark_task_completed():
    view_tasks()
    task_num=int(input("Enter the task number to mark as completed: ")) -1
    if 0<=task_num<len(tasks):
        tasks[task_num]["completed"]=True
        input("Task marked as completed.Press enter to continue...")
    else:
        input("Invalid task number.Press enter to continue...")
def delete_task():
    view_tasks()
    task_num = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        del tasks[task_num]
        input("Task deleted. Press Enter to continue...")
    else:
        input("Invalid task number. Press Enter to continue...")
while True:
    show_menu()
    choice=input("Enter your choice(1/2/3/4/5): ")
    
    if choice=='1':
        add_task()
    elif choice=='2':
        view_tasks()
    elif choice=='3':
        mark_task_completed()
    elif choice=='4':
        delete_task()
    elif choice=='5':
        exit()
        break
    else:
        print("Invalid choice.Press enter to continue...")
