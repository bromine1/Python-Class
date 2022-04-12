#3-2-1-15
class QueueError(ValueError):  # Choose base class for the new exception.
    pass # Just an extra error for user processing


class Queue:
    def __init__(self):
        self.que = [] #start the que
    
    def put(self, elem):
        self.que.append(elem) # apply to end of que
    
    def get(self): # take from part of que
        try:
            val = self.que[0]
            del self.que[0]
            return val
        except ValueError:
            raise QueueError # raise special error
class SuperQueue(Queue): #extend class functionality
    def __init__(self): #initialize class
        super().__init__() # super initializes the super class: good if I change names or super classes
    
    def isempty(self): # function to tell if something is empty
        if len(self.que) == 0:
            return True

#Test Data
que = SuperQueue() 
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

