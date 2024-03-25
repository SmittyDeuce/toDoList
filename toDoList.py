from tabulate import tabulate

def toDoList():
    menu = ["1) add a task", "2) view tasks", "3) mark a task as complete",
            '4) delete a task', '5) quit']
    
    print("Welcome to The To-Do List App!")
    print(tabulate([[option] for option in menu], headers=["Menu"], tablefmt="pipe"))
    
while True:
    tasks = []
    try:
        menuOption = int(input("Please choose a menu option: "))
        if menuOption == 5:
            print("Thank you for using our app!")
            break

        elif menuOption == 1:
            print("Add a task")
            while True:
                addTask = input("What task would you like to add?: ('done' when finshed) ")
                addTask = addTask.lower()
                if addTask == 'done':
                    break
                else:
                    tasks.append(addTask)
                    
        else:
            pass
    except ValueError:
        print("Please enter a number 1-5 ")
        continue  


toDoList()