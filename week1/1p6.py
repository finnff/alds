# 1:
def avgHairLength(arr):
    sum = 0
    count = 0
    for i in arr:
        sum = sum + i
        count = count + 1
    return (sum/count)


def hairy(arr):
    result = []
    m = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = (avgHairLength(tup) -
                                (avgHairLength(arr)/avgHairLength(tup)))
                yeet = (tup, relativeHair)
                result.append(yeet)
                m += 1
    return result


list2 = [11, 22, 33, 54, 65, 26, 27, 38, 59, 67, 25, 23, 32, 51, 64, 27, 29, 38, 50, 63, 22, 21,
         31, 52, 63, 24, 25, 36, 57, 68, 29, 27, 35, 53, 62, 21, 24, 37, 59, 68, 20, 23, 32, 51,
         11, 22, 33, 54, 65, 26, 27, 38, 59, 67, 25, 23, 32, 51, 64, 27, 29, 38, 50, 63, 22, 21,
         31, 52, 63, 24, 25, 36, 57, 68, 29, 27, 35, 53, 62, 21, 24, 37, 59, 68, 20, 23, 32, 51,
         11, 22, 33, 54, 65, 26, 27, 38, 59, 67, 25, 23, 32, 51, 64, 27, 29, 38, 50, 63, 22, 21,
         31, 52, 63, 24, 25, 36, 57, 68, 29, 27, 35, 53, 62, 21, 24, 37, 59, 68, 20, 23, 32, 51,
         11, 22, 33, 54, 65, 26, 27, 38, 59, 67, 25, 23, 32, 51, 64, 27, 29, 38, 50, 63, 22, 21,
         31, 52, 63, 24, 25, 36, 57, 68, 29, 27, 35, 53, 62, 21, 24, 37, 59, 68, 20, 23, 32, 51]

# 2 O(N^4)

# 4  O(N^3)


def hairyimporved(arr):
    result = []
    m = 0
    arrayavglength = avgHairLength(arr)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                tupleavglength = avgHairLength(tup)
                relativeHair = (tupleavglength -
                                (arrayavglength/tupleavglength))
                yeet = (tup, relativeHair)
                result.append(yeet)
                m += 1
    return result



hairy(list2)
# hairyimporved(list2)


#

"""
default runtime    O(N^4):

real    0m7,302s
user    0m7,258s
sys     0m0,045s

improved runtime   O(N^3):

real    0m0,685s
user    0m0,638s
sys     0m0,044s



different system loads at moment of exection can influence results.
timing doesnt say alot about scaling, and worst case performance is 
usually more interesting when implenting algorithms.
"""
