"""
Parameters 
--------
Arr:
    List of Ints/ Floats/ chars
n:
    number to find

Return
-------
  index of array where find() locates n

find() = O(n)


"""

# start from the end beacuse length
def find(arr, n):
    if not arr:
        return -1
    if arr[0] == n:
        return 0
    temp = find(arr[1:], n)
    if temp is not -1:
        return (1 + temp, n)
    else:
        return -1


list0 = []
list1 = [1, 2, 3, 48, 5, 18182838127, 18182838127, 8, 9]
list2 = [1.1, 2.1, 3.82, 4.27, 5.2, 6.2, 7.3, 8.2, 9.9]
list3 = [1, 2, 3, 4, 5, 'E', 'A', 'z', 9]
list4 = [1, "test", 3, 4, 5, 'Ez', 'Az', 'UZ', 9]


print(find(list0, 48))
print(find(list1, 48))
print(find(list2, 9.9))
print(find(list3, 'r'))
