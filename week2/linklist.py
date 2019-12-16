class linkedList():
    def __init__(self, value=None):
        self.value = value
        self.tail = None

    def append(self, value):
        if self.tail is None:
            self.tail = linkedList(value)
        else:
            self.tail.append(value)

    def print(self):
        print(self.value)
        if self.tail:
            self.tail.print()

    def delete(self, value, prev=None):
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
        if self.tail is None:
            return self.value
        tmp = self.tail.min()
        if tmp < self.value:
            return tmp
        return self.value


