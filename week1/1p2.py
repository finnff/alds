"""
Parameters 
--------
str:
    String

Return
-------
  list with numbers found within the string


getNumbers() = O(n)




"""


def getNumbers(str):
    output = []
    tempvalue = 0
    index = 0
    for i in str:
        index += 1  # fuck python
        if i.isdigit():
            tempvalue = tempvalue * 10
            tempvalue = tempvalue + int(i)
        if (not (i.isdigit()) or index == len(str)):
            if tempvalue != 0:
                output.append(tempvalue)
                tempvalue = 0
    return output


str1 = "een1293zin45 6met-632meer9dere+7777getallen89"

print(getNumbers(str1))
