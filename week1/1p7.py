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


def find(arr, n):
    if arr[0] == n:
        return 0
    return 1 + find(arr[1:], n)




list1 = [1, 2, 3, 48, 5, 18182838127, 18182838127, 8, 9]
list2 = [1.1, 2.1, 3.82, 4.27, 5.2, 6.2, 7.3, 8.2, 9.9]
list3 = [1, 2, 3, 4, 5, 'E', 'A', 'z', 9]
list4 = [1, "test", 3, 4, 5, 'Ez', 'Az', 'UZ', 9]

print(search(list1, 48))
print(search(list2, 9.9))
print(search(list3, 'z'))
print(search(list4, 'Az'))

