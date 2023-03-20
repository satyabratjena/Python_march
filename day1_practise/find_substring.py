def string(main,substring):
    count = 0
    for i in main:
        if i ==substring:
            count +=1

        if count == 0:
            return-1
        else:
            return count


def substring():
    main = input("Enter the main string: ")
    substring = input("Enter the substring: ")
    result = main.find(substring)
    print(f'Substring {substring} found at index:', result)

substring()
