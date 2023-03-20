#copy paste 3examples on class and object 

#1/

class Cylinder:
    pi = 3.14
    
    def __init__(self, radius, height):

        # instance variables
        self.radius = radius
        self.height = height
 
    # instance method
    def volume(self):
        return Cylinder.pi * self.radius**2 * self.height
 
    # class method
    @classmethod
    def description(cls):
        return f'This is a Cylinder class that computes the volume using Pi={cls.pi}'
         
if __name__ == '__main__':
    c1 = Cylinder(4, 2) # create an instance/object
 
    print(f'Volume of Cylinder: {c1.volume()}') # access instance method 
    print(Cylinder.description()) # access class method via class
    print(c1.description()) # access class method via instance

#2/


class Bike:
    name = ""
    gear = 0

bike1 = Bike()

bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")




#3/

class add_sub:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # define 'add' method
    def add(self):
        return self.x + self.y
    # define 'subtract' method
    def subtract(self):
        return self.x - self.y
 
if __name__ == '__main__':
    x = 10
    y = 6
    # create an instance 
    opp = add_sub(x,y)
 
    # call add method
    print(f'{x} + {y} = {opp.add()}')
    #print(opp.add())
 
    # call subtract method
    print(f'{x} - {y} = {opp.subtract()}')