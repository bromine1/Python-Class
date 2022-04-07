#3-2-1-15
class QueueError(ValueError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.que = []
    
    def put(self, elem):
        self.que.append(elem)
    
    def get(self):
        try:
            val = self.que[0]
            del self.que[0]
            return val
        except ValueError:
            raise QueueError
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        if len(Queue.que) == 0:
            return True

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

