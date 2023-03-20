from task import Task

dict = {}

def ispresent(word):
    if dict.get(word) in not None:
        return True
    else:
        return "The ID is not there"

def Add(word,value):
    dict[word] = value
    return "Task has been added successfully"

def update(word):
    if word not in dict:
        return "Task has been updated successfully"

def view(word):
    if word in dict:
        return dict[word]
    else:
        return "The word is not there"

def Remove(word):
    return "Removed",dict.pop(word)