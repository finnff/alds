class myStack():
    """container that functions as a stack, with isEmpty,push, pop,
    and peek functions initialization requires no parameters
    """

    def __init__(self):
        """Initializes an empty stack
        """
        self.arr = []

    def isEmpty(self):
        """boolean Check if stack is empty, and returns a true/false
        """
        if(self.arr == []):
            return True
        else:
            return False

    def push(self, x):
        """addes x to the Stack
        """
        self.arr.append(x)

    def pop(self):
        """Removes the last item from the Stack and returns this value
        """
        if not self.isEmpty():
            return(self.arr.pop())
        return None

    def peek(self):
        """Returns the last item on the stack without removing it
        """
        if not self.isEmpty():
            return self.arr[-1]
        return None