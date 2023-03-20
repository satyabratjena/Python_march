from dictpres import *

dict = {}

def addWord(word):
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1
        return "Word has been added"

def viewAll():
        return dict
    
def viewwithOccurs():
    return dict.items()

def viewWithInput(i):
     emt = []
     for n in i:
        if dict(n) in i:
         return emt.append(i)
     else:
         return "Word not found"