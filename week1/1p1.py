
def mymax(a):
  if (len(a)==0):
    print("Empty List")
  # index = 0
  for index in a:
    if ((isinstance(a[index-1], int)) ):
      print("yeet yeet")
    else:
      print("List containt non int values")







list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [1.1, 2.1, 3.82, 4.27, 5.2, 6.2, 7.3, 8.2, 9.9]
list3 = [1, 2, 3, 4, 5, 'a', '@', 'U', 9]
print(mymax(list1))
# print(mymax(list2))
# print(mymax(list3))
