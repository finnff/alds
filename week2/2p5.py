import linklist

l = linklist.linkedList(7)
l.append(2)
l.append(3)
l.append(3)
l.append(0)
l.append(5)
l.append(6)
l.delete(0)

print(l.min())
l.print()
