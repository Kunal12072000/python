from sys import maxsize
def createstack():
    stack = []
    return stack
def isstackempty(stack):
    return (len(stack) == 0)
def push(stack,item):
    stack.append(item)
    print(item , "pushed to the stack")
def pop(stack):
    if (isstackempty(stack)):
        return str(-maxsize-1)
    return stack.pop()
def peek(stack):
    if(isstackempty(stack)):
        return str(-maxsize-1)
    return stack[len(stack) - 1]
stack = createstack()
push(stack,10)
push(stack,20)
push(stack,30)
print(peek(stack))
print(pop(stack))


