import timeit

def avgHairLength(arr):
    total =0
    for i in arr:
        total=total + i
    return total


def Hairy(arr):
    result = []
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(arr) - avgHairLength(tup)
                result = (tup, relativeHair)
    return result


# exited with code=0 in 13.838 seconds 100 000 iterations


list1 = [1,2,3,4,5,6,7,8,9]


### O = N ^ 4 Due to for loop being calling in function avgHairLength

### 

def avgHairLength2(arr):
    total =0
    for i in arr:
        total=total + i
    return total


def Hairy2(arr):
    result = []
    average = avgHairLength2(arr)
    for i in range(0, len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = average - avgHairLength2(tup)
                result = (tup, relativeHair)
    return result

list1 = [1,2,3,4,5,6,7,8,9]



## exited with code=0 in 10.505 seconds na 100 000 iterations
## could be faster still by calculating tuple directly rather than iteration for loop again

