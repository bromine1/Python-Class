class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        val = self.stack[-1]
        del self.stack[-1]
        return (val)

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
    self.__sum = 0



stack_object = Stack()  # Instantiating the object.

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)


print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())