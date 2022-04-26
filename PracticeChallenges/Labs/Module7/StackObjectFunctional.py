stack = []

#Values must be defined as global to work everywhere
def push(val):
    global stack
    stack.append(val)

def pop():
    global stack
    val = stack[-1]
    del stack[-1]
    return val

push(1)
print(pop())









