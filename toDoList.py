from tabulate import tabulate

def toDoList():
#  from here down it handles the init app greeting, and user interface
# displaying the differnt options availale.
      
    tasks = {"incomplete":[], "complete":[]}
    while True:
        menu = ["1) add a task", "2) view tasks", "3) mark a task as complete",
            '4) delete a task', '5) quit']
    

        print("Welcome to The To-Do List App!\n", "")

        menuTable = tabulate([[option] for option in menu], headers=["Menu"], tablefmt="pipe")
        print(menuTable)
        menuOption = input("Please choose a menu option: ")
        try:
            menuOption = int(menuOption)
            print(menuTable)
            if menuOption == 5:
                print("Thank you for using our app!")
                break
# from here down it handles menu option 1:
            elif menuOption == 1:
                print("Add a task")
                while True:
                    addTask = input("What task would you like to add?: ('done' when finshed) ")
                    addTask = addTask.lower().strip()
                    if addTask == 'done':
                        break
                    if addTask in tasks["incomplete"] or addTask in tasks["complete"]:
                        print("Error: task already exists")
                        continue
                    else:
                        tasks["incomplete"].append(addTask)
# from here down is menu option 2:
            elif menuOption == 2:
                print("Current Tasks")
                print(tasks)
                while True:
                        finishedViewing = input("enter 'done when finished ")
                        finishedViewing = finishedViewing.lower().strip()
                        if finishedViewing == 'done':
                            break
                        else:
                            print("please enter 'done' when finished")
                            continue
#  from here down handles menu option 3
            elif menuOption == 3:
                print("Mark Task as Complete")
                while True:
                    completedTask = input("What tasks have been completed: (enter 'done' when finished) ")
                    completedTask = completedTask.lower().strip()
                    if completedTask == 'done':
                        break
                    else:
                        taskFound = False
                        for status, task in tasks.items():
                            if completedTask in task:
                                tasks["complete"].append(completedTask)
                                tasks["incomplete"].remove(completedTask)
                                taskFound = True
                                print("Task marked completed\n",  tasks['complete'])
                                break
                        if not taskFound:
                            print("Error: Task Not Found")
                    

        except ValueError:
            print("Please enter a number 1-5 ")
            continue  


toDoList()