# print("Hello World")

def num(x,y):
    return x+y

def num2():
    x = int(input("Number for x: "))
    y = int(input("Number for y: "))
    sum = x+y
    print(sum)

# def num(x):
#     return x*7

# f = 3

# l1 = num(f)
# print(l1)

# logic part 
# here we are only writing the logic, (not giving any print statement.)
def getfullname(first,last):
    return ("The  name you entered is" ,first+last)

# presentation part
# here we are presenting as pring things and taking input from the user
def start():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")

    name = getfullname(fname,lname)
    print(name)

start();

###################################
###################################

#2//// 
def getValue(a,b):
    a,b = b,a

    return (a,b)

def value():
    x = int(input("Enter the operand: "))
    y = int(input("Enter the operand: "))
    swap = getValue(x,y)
    print(swap)

value();

#####################
#/

def multiplyNum(num1):
    return num1*8

def Multiplicate():
    result = multiplyNum(9)
    print("result is", result)

Multiplicate();

################
#3/

def substract(x,y):
    result = x-y
    return result

def startTheApp():
    x = float(input("Enter first operand:"))
    y = float(input("Enter first operand:"))
    z = substract(x,y)
    print("result is", z)

startTheApp();