from logic import 

def init():
    exit = False

    while exit == False:
        print("** Main Menu **")
        print("1. Enter the TaskId")
        print("0. Exit")
    
        choice = int(input("Enter your choice: "))

        if ch == 1:
            task_input = int(input("Enter the TaskId: "))
            task(task_input)
        
        elif ch == 0:
            exit = True

def task():
    if op == 1:
        while is not True:
            task_input = int(input("Enter the TaskId: "))
            option = messsage(task_id)
        
        if ch == True:
            print("** -2nd Menu- **")
            print("1. Update task details")
            print("2. Remove task details")
            print("3. view task details")
            print("0. Back to menu")
        else:
            print("** Task ID not Found **")
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            prio = int(input("Enter priority: "))
            due_Add = Task(task_input, name, description, prio)
            add(due_Add)

    elif op == 2:
        message = view()
        print(messsage)

    elif op == 0:
        exit =True
        print("Goodbye")