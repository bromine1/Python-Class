class Stack: # create stack class and initialise list
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val






















class CountingStack(Stack): # Start the counting class
    def __init__(self):
        Stack.__init__(self)
        self.count = 0

    def get_counter(self): # Create the counter function
        return(self.count)

    def pop(self): # Modify pop to count items exited
        self.count += 1
        Stack.pop(self)

#Test data
stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())