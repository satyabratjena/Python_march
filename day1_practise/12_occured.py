def occured(list1):
    most_occured = 0
    for lists in list1:
        str1 = list1.count(lists)
        if str1 > most_occured:
            str1, most_occured = most_occured, str1
    return most_occured

def start():
    lists = [1,2,6,2,2,4,5]
    result = occured(lists)
    print(result)

start();