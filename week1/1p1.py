"""
Parameters 
--------
Arr:
    List of Ints, Floats, chars

Return
-------
    Currmax(Int, Float, Char depending on Array)
    Returns CurrentMaximum at end of for loop, resulting in highest value item.



MyMax() = O(n)



"""


def MyMax(arr):
    if (len(arr) == 0):
        print("Empty List")
        return -1
    else:
        currmax = arr[0]
        for item in arr:
            if (item > currmax):
                currmax = item
        return currmax


list1 = [1, 2, 3, 48, 5, 18182838127, 18182838127, 8, 9]
list2 = [1.1, 2.1, 3.82, 4.27, 5.2, 6.2, 7.3, 8.2, 9.9]
list3 = [1, 2, 3, 4, 5, 'E', 'A', 'z', 9]
list4 = [1, "test", 3, 4, 5, 'Ez', 'Az', 'UZ', 9]
list5 = []


print(MyMax(list1))
print(MyMax(list2))
print(MyMax(list3))
print(MyMax(list4))
print(MyMax(list5))
