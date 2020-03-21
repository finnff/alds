class linkedList():
    """initialize a empty linked list"""
    def __init__(self, value=None):
        self.value = value
        self.tail = None

    """add a value to the linked list, 
    """
    def append(self, value):
        if self.tail is None:
            self.tail = linkedList(value)
        else:
            self.tail.append(value)

    def print(self):
        """Prints every value in the linked list on a new line
        """
        print(self.value)
        if self.tail:
            self.tail.print()

    def delete(self, value, prev=None):
        """removes all values from the linked list. Prev parameter is
        used for internal recursion and shouldnt be used.
        """
        if prev is None:
            if self.value is value:
                self.value = self.tail.value
                self.tail = self.tail.tail
                self.delete(value)
            self.tail.delete(value, self)
        elif self.tail is None:
            if self.value is value:
                prev.tail = None
        elif self.value is value:
            prev.tail = self.tail
            prev.tail.delete(value, prev)
        else:
            self.tail.delete(value, self)

    def min(self):
        """Returns the lowest/minimum value from the linked list.
        """
        if self.tail is None:
            return self.value
        tmp = self.tail.min()
        if tmp < self.value:
            return tmp
        return self.value


