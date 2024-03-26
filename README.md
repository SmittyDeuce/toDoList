# toDoList
Greetings to all! this will be the first of 5 projects I will be working on. I will be attemping a to do list project using python. There are a 
few things that I be the main focus of me trying to implement into file.
start date 02/14/24

1) Add Tasks
2) Mark tasks as completed
3) delete tasks
4) view current tasks


2/18/24
added inputs for asking for errands as well as for "anything else" createad an
if statement for initial chore and nested inside a while loop stating that while
anything else != '' continue to ask.. all that works fine but my current else "why are you here go enjoy your day" prints regardless if the list that I created called toDo is empty or not when, I want it to only print if toDo is empty.


3/23/2024

turns out coding temple is having me do a to do list project so i will scrap my original and start over from a clean slate.. it feels better that way for me but i will still attempt to implement my 4 requirements:
    1. add tasks
    2. mark tasks as completed
    3. delete tasks
    4. view current tasks

1) User Interface
    1. Create a command line interface for the application
    2. display welcome message and menu with following options:
        Welcome to the To-Do List App!
        Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit

2) To-Do List Features:
    1) Implement the follwing features for the List:
        1. adding a task with a title (by default 'incomplete')
        2. Viewing the list of tasks with their titles and statuses 
           (e.g., "Incomplete" or "Complete").
        3. Marking a task as complete.
        4. Deleting a task.
        5. Quitting the application.

3) User Interaction
    Allow users to interact with the application by selecting menu options using input().
    Implement input validation to handle unexpected user input gracefully.

4) Error Handling:
    1. Implement error handling using try, except, else, and finally blocks to handle potential issues.


5) Code Organization:
    1. Organize your code into functions to promote modularity and readability.
    2. Use meaningful function names with appropriate comments and docstrings for clarity.


6) Testing and Debugging:
    1. Thoroughly test your application to identify and fix any bugs.
    2. Consider edge cases, such as empty task lists or incorrect user input.


7. Documentation:
    1. Include a README file that explains how to run the application and provides a brief overview of its features.


8. Optional Features (Bonus):
    1. If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.


9. GitHub Repository:
    1. Create a GitHub repository for your project.
    2. Commit your code to the repository regularly.
    3. Include a link to your GitHub repository in your project documentation.



I imported tabulate because i wanted the ""gui"" to be in the a table format
had some trouble initialy because the table would print but each word had its own column. In order to fix it i had to iterate though my "menu" list but had to make each element its own list ['option'] => ['add a task] which gave me what i was looking for.


3/24/2024

started off trying to get my value error exception to work I was forgetting my else: statement inside my try block which was giving me the issue. now I will work on filling how other errors as well as, Option one which is 'add a task'
    added nested while true to take into the account if user wants to keep adding a task, only to exit once they enter 'done' which will send them back to menu.
rearranged the code to display the menu option table each time the user goes back into the main screen at first it was just show on init call of func.
    was able to do option 2: view tasks, I created an input that gives user to exit when typing 'done' and only done. 
ValueError exception stopped working will need to fix that turned task from list into a dictonary to add incomplete and complete as keys so i can work my way towards filtering by that as well as marking tasks as complete


3/25/24

eception was not broke i was just over looking it, also was able to do menu option 3 as well as, finish up option 4 'delete a task" and my final else statement that accounts for anthying outside of value error and int 1-5