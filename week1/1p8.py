"""
Parameters 
--------
a:
    int

b:
  int 

Return
-------
  Largest common divisor for a/b 


getNumbers() = O(n)



"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(144, 873))
