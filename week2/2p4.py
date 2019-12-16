import random
import statistics


def partitionHigh(arr, low, high):
    """
    Parameters
    ----------
    arr: list
            arr of numbers
    low:
            lowest index of arr
    high:
            highest index of the arr
    Returns
    -------
    arr : list
            return the list
    comparisons : int
            comparisons has counted how many times two values are compared
    """
    pivot = arr[high]
    i = low
    comparisons = 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]

    return i, comparisons


def partitionLow(arr, low, high):
    """Same as Above Partition High, but with Low pivot instead
    """
    pivot = arr[low]
    i = low
    comparisons = 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]

    return i, comparisons


def partitionMed(arr, low, high):
    """Same as Above Partition High, but with Low pivot instead
    """
    pivot = statistics.median(arr)
    i = low
    comparisons = 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[i], arr[high] = arr[high], arr[i]

    return i, comparisons


def quickSort(arr, low, high):
    """
    Parameters
    ----------
    arr: list
            arr of numbers
    low:
            lowest index of arr
    high:
            highest index of the arr
    Returns
    -------
    arr : list
            return the list
    comparisons : int
            comparisons has counted how many times two values are compared
    """
    comparisons = [[], [], []]
    if low >= high:
        return arr, 1
    p, comparisons[0] = partitionLow(arr, low, high)
    arr, comparisons[1] = quickSort(arr, low, p-1, )
    arr, comparisons[2] = quickSort(arr, p+1, high, )
    return arr, sum(comparisons)+1


# 4.1 + 4.2
list1 = [13, 123, 765, 13, 46, 7, 8, 6, 2323, 235]
print(quickSort(list1, 0, len(list1)-1))


# 4.3 Run time appears to be sub-linear of N?
for i in range(0, 10000):
    list2 = []
    for j in range(0, 200):
        list2.append(random.randrange(1, 100))
    print(quickSort(list2, 0, len(list2)-1))


# 4.4
    # See PartitionLow and change QuickSort call accordingly



# 4.5+4.6
# Runtime appears to be slightly higher when min is used instead of Max,
# however the number of comparisons done is alot higher on average(approx 5x as much?)


#4.7
#(10000 loops of 200 number long lists)

#Runtime Using Min
# real    0m22,333s (aprox 11k comparisons)

#Runtime Using High
# real    0m6,616s (aprox 2k comparisons)

# Runtime Using Median
# real    0m35,159s (always 104xx comparisons)



#Looking at runtime, Median is a terrible choice but this may be because
#Calling the statistic.Median() function isnt optimal.

#High is substantially Faster than Both Median, and Low in runtime and comparisons
#Low preforms better than Median, but logically shouldnt.
#Comparison wise Median and Low should be around the same time, how ever this was not the Case.












