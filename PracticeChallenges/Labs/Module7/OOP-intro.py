#Ryan Stauffer
#4
#Python Programming II ~ Object-Oriented Programming
#3.1.1.0 to 3.1.1.8 The foundations of OOP
#3.2.1.1 to 3.2.1.13
#April 5, 2022 to April 7th, 2022
#Instructions: Provide a programming example for each section. Be certain you have added the programming comments with your new found learning knowledge or prior knowledge. In addition, answer the following two reflection questions.



#Procedural vs. the object-oriented approach
#mammals ( )
#reptiles (turtle)
#birds ( )
#fish (shark )
#amphibians (frog, )

#Objects are pieces of code that store data and methods that act upon data

#What is an object?
#A class (among other definitions) is a set of objects. An object is a being belonging to a class.

#What does an object have?
#Two sample phrases should serve as a good example:

#A pink Cadillac went quickly.

#Object name = Cadillac
#Home class = Wheeled vehicles
#Property = Color (pink)
#Activity = Go (quickly)

#Not sure what to put here

#It's time to define the simplest class and to create an object. Take a look at the example below:
#We've defined a class there. The class is rather poor: it has neither properties nor activities. It's empty, actually, but that doesn't matter for now. The simpler the class, the better for our purposes.

class TheSimplestClass:
    pass #The pass keyword fills the class with nothing. It doesn't contain any methods or properties.

#Your first object
my_first_object = TheSimplestClass()

#the stack approach
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

#Stacks can be done procedurally, but it makes more sense to use an object
#This way you can partition data and collaborate

#Example of stack class done in OOP

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.stack = []
    
    def push(self, val): 
        self.stack.append(val)
    
    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return (val)

stack_object = Stack()  # Instantiating the object.
Stack_object_dos = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

Stack_object_dos.push(4)
Stack_object_dos.push(5)
Stack_object_dos.push(6)

print(stack_object.stack)
print(Stack_object_dos.stack)


print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

#Recap and Review Questions:  
#Instructions: answer with complete sentences and support your responses with learning evidence.

#1. What was the most important thing you learned from the lesson reading and coding examples? 

#Objects are awesome ways to encapsulate and work with data, although they can be a bit confusing
#Its best to write objects in a clear and sensible way
#Remember, if you can't maintain and debug it, it isn't good code


#2. Why is it important? Give specific reasons and examples.

#Objects allow us to store and create large volumes and sets of data, as well as work with them, without maintianing large files
#Moreover, it lets us make distinctions with different objects
#and we cna use inheritance and more to extend how we can manipulate the data.