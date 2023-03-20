from dictlogic import addWord, viewAll, viewwithOccurs, viewWithInput

def init():

    exit = False

    while exit == False:
        print("*** MENU ***")
        print("1. Add a word")
        print("2. view all words.")
        print("3. show all words with number of time it occurs.")
        print("4. view all words with input as how many times it occurs.")

        print("0. Exit")
        ch = int(input("Enter your choice:"))

        if ch == 1:
            word = input("Enter the word")
            message = addWord(word)
            print(message)
            print()

        elif ch == 2:
            message = viewAll()
            print(message)
            print()

        elif ch == 3:
            i = int(input("Enter the occured num : "))
            message = viewwithOccurs(i)
            if not message:
                print("No such word")
            else:
                print(i, "has occured", message)

        elif ch == 4:
            item = int(input("Enter the num : "))
            message = viewWithInput(item)
            print(message)
            print()


        elif ch == 0:
            print("--- GoodBye! ---")
            break