

def Hairy(arr):
    result = []
    m = 0
    for i in arr.size():
        for j in i:
            for k in j:
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(tup) - avgHairLength(arr / tup)
                result[m] = (tup, relativeHair)
                m = m+1
    return result
