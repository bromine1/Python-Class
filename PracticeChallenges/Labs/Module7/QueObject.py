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

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")

