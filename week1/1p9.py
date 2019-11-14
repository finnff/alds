"""

1. For i < 1000, check if i is divisible by any of the earlier numbers tested (2.Terrible idea, O=n!)


3

Parameters 
--------
n:
    int

Return
-------
  null, but print all Primes between 2 and n


sieve() = O(n^2)
"""


def sieve(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            print(i)
            for j in range(i*i, n+1, i):
                multiples.append(j)


# sieve(50000)


# 4 de sieve of Eratosthenes kan op meerdere wijzes geimplementeerd worden,
# de bovenste sieve() functie heeft een O=n maar de onderstaande eratosthenes() complexity van O=log(n)
# dit komt omdat yield efficienter werkt?
# https://www.rosettacode.org/wiki/Sieve_of_Eratosthenes#Python

def eratosthenes2(n):
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


print(list(eratosthenes2(10000)))


