
class PrioQue():
    """
    ADT with a value and a priority,
    Lower priorty items will be dequed 1st
    """

    def __init__(self):
        """Initializes an empty stack
        """
        self.arr = []

    def __str__(self):
        return ' '.join([str(i) for i in self.arr])

    def queue(self, value, prio):
        self.arr.append([prio, value])

    def dequeue(self):
        temp = min(self.arr)
        self.arr.remove(min(self.arr))
        return temp

    def contains(self, value):
        for items in self.arr:
            if items[1] == value:
                return True
            else:
                return False

    def remove(self, value):
        for items in self.arr:
            if items[1] == value:
                self.arr.remove(items)


q = PrioQue()
q.queue(15, 2)
q.queue(15, 2)
q.queue(15, 2)
q.queue(15, 8)
q.queue(15, 17)
q.queue(15, 9)
q.queue(15, 7)
q.queue(92, 1)
q.queue(128, 1)
q.queue(52, 1)
q.queue(81, 1)
q.queue(73, 14)
q.queue(5, 8)
print(q.contains(15))
print(q.dequeue())
q.remove(15)
q.queue(28, 1)
q.queue(73, 14)
q.queue(5, 8)
print(q.contains(15))
print(q.dequeue())
print(q)

# print(q)
