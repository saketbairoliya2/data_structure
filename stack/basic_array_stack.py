# This is a smaple code for stack implementatin.

# Push, pop and pick, isEmpty
from sys import maxsize

def create_stack():
    stack = []
    return stack
    
def push(self, data):
    self.append(data)
    
def isEmpty(stack):
    return len(stack) == 0
    
def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize - 1)
    return stack.pop()

stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
print(pop(stack))
print(pop(stack))


    