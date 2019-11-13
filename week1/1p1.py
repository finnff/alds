
def mymax(arr):
    if (len(arr) == 0):
        print("Empty List")
    else:
        currmax = arr[0]
        for item in arr:
            if (item > currmax):
                currmax = item
        return currmax


list1 = [1, 2, 3, 48, 5, 18182838127, 18182838127, 8, 9]
list2 = [1.1, 2.1, 3.82, 4.27, 5.2, 6.2, 7.3, 8.2, 9.9]
list3 = [1, 2, 3, 4, 5, 'E', '@', 'U', 9]
print(mymax(list1))
print(mymax(list2))
print(mymax(list3))
