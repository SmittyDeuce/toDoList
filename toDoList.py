from tabulate import tabulate

def toDoList():
    menu = ["add a task", "view tasks", "mark a task as complete",
            'delete a task', 'quit']
    
    print("Welcome to The To-Do List App!")
    print(tabulate([[option] for option in menu], headers=["Options"], tablefmt="pipe"))







toDoList()