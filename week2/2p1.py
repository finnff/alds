import Stack

stack = Stack.myStack()

print(stack.isEmpty())
stack.push(15)
print(stack.peek())
stack.push(5)
print(stack.peek())
print(stack.pop())
print(stack.peek())
print(stack.isEmpty())
