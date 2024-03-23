from tabulate import tabulate
# I want the CLI to appear as a table

def toDoList():
    menu = ["add a task", "view tasks", "mark a task as complete",
            'delete a task', 'quit']
    
    print("Welcome to The To-Do List App!")
    print(tabulate([[option] for option in menu], headers=["Options"], tablefmt="pipe"))

    # called on tabulate so i can create table with 'plain' format

    # [[option] for option in menu] iterated through menu and turned
    # element into its own list ex['add a task'] otherwise my table was
    # giving each word its own block


    




toDoList()