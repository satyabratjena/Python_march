import random

listItem = []

def randomNum():
    for i in range(10):
        listItem.append(random.randint(10,50))
    return listItem

def viewAll():
    return listItem

def updateNum(a,b):
    if a not in listItem:
        return "Number is not there in the List."
    elif b in listItem:
        return "Number is already there in the list."
    else:
        i = listItem.index(a)
        listItem[i] = b
        return "Updated the number successfully."

def removeNum(i):
    if i in listItem:
         list.remove(i)
         return "Removed the number successfully."
    else:
        return "Number is not there in the list."

def asc():
    asc = listItem.copy()
    asc.sort()
    return asc

def desc():
    desc = listItem.copy()
    desc.sort(reverse=True)
    return desc