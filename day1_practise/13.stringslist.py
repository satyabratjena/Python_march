def string_list(list):
    result = []
    for j in list:
        result.append(len(j))
    return result

def string():
    list = ["hi","here are imp things","How you doing"]
    message = string_list(list)
    print(message)

string();