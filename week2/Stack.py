class myStack():
    """container that functions as a stack, with isEmpty,push, pop,
    and peek functions
    """

    def __init__(self):
        """Initializes an empty stack
        """
        self.arr = []

    def isEmpty(self):
        """Checks if stack is empty, and returns a boolean
        """
        if(self.arr == []):
            return True
        else:
            return False

    def push(self, x):
        """Appends x to the Stack
        """
        self.arr.append(x)

    def pop(self):
        """Removes the last item from the Stack and returns this value
        """
        return(self.arr.pop())

    def peek(self):
        """Returns the last item on the stack
        """
        return self.arr[-1]


