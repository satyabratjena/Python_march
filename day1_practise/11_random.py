import random

def ran_list():
    list = []
    for j in range(10):
        list.append(random.randint(10, 20))
    return list

def randomList():
    randomList = ran_list()
    print(randomList)

randomList();