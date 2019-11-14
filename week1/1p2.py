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
  for i in str:
    if i.isdigit():
      tempvalue = tempvalue * 10
      tempvalue = tempvalue + int(i)
    else:
      if tempvalue != 0 :
        output.append(tempvalue)
        tempvalue =0

  return output


str1 = "een123zin45 6met-632meerdere+7777getallen"

print(getNumbers(str1))