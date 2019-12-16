import random
from datetime import datetime
random.seed(datetime.now())


def checkSame(arr):
    """
    Parameter:
    ----------
      arr : List

    Return:
    ----------
      Boolean: True if list contains duplicates, otherwise False
    """
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False


def BirthdayProblem(NumStudents):
    """
    Parameter:
    ----------
      NumStudents: Integer, that simulates the amount of people in group
      for Birthday Paradox.


    Return:
    ----------
      Float: Probability() of two students have the same birthday

    """
    dups_found = 0
    for _ in range(100):
        arr = [random.randrange(1, 365)for _ in range(NumStudents)]
        if checkSame(arr):
            dups_found += 1
    return (dups_found / 100.0)


print(BirthdayProblem(23))
print(BirthdayProblem(70))


# 99.9% probability is reached with just 70 people, and 50% probability with 23 people.
# from https://en.wikipedia.org/wiki/Birthday_problem#A_simple_exponentiation
# Tested values seem to correspond with this
