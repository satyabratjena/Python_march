from logic import randomNum, viewAll, updateNum, removeNum, asc, desc



def init():

    exit = False

    while exit == False:
        print("*** MENU ***")
        print("1. Fill up list with 10 random numbers")
        print("2. view all the list")
        print("3. change a number in the list")
        print("4. remove element in the list")
        print("5. Sort in ascending")
        print("6. Sort in descending")
        print("0. Exit")
        ch = int(input("Enter your choice:"))
        if ch == 1:
            message = randomNum()
            print(message)
            print()

        elif ch == 2:
            message = viewAll()
            print(message)
            print()

        elif ch == 3:
            a = int(input("Enter the number: "))
            b = int(input("Enter the update number: "))
            message = updateNum(a,b)
            print(message)
            print()

        elif ch == 4:
            item = int(input("Enter the num which is to be removed: "))
            message = removeNum(item)
            print(message)
            print()

        elif ch == 5:
            message = asc()
            print(message)
            print()

        elif ch == 6:
            message = desc()
            print(message)
            print()

        elif ch == 0:
            print("--- GoodBye! ---")
            break
        