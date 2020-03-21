

"""
Parameters
--------
I:
    int
    Number used in recursion to keep track of matrix position

J:
  int
  Input amount that is being calculated

coins:
    list
    List of availible Coin/Banknotes that amount can be payed in.

A:
    nested list
    Matrix used for the calculation of posibilitys of paying amount J.


Return
-------
  Amount of  different distinct combinations of coins
  and bank notes the input can be paid in.


"""


def amounthandler(I, J, coins, A):
    if J < 0:
        return 0
    if A[I][J] == -1:
        if J == 0:
            A[I][J] = 1
        elif I == 0:
            A[I][J] = 1
        elif J >= coins[I]:
            A[I][J] = amounthandler(
                I-1, J, coins, A) + amounthandler(I, J-coins[I], coins, A)
        elif J < coins[I]:
            A[I][J] = amounthandler(
                I-1, J, coins, A)
    return A[I][J]


"""
Parameters
--------
amount:
  int
  Input amount

Return
-------
  Amount of  different distinct combinations of coins
  and bank notes the input can be paid in.

"""


def possibiltyCalc(amount):
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    matrix = []
    value = []

    for _ in range(amount+1):
        value.append(-1)
    for _ in range(len(coins)):
        matrix.append(value)

    return amounthandler(12, amount, coins, matrix)


print(possibiltyCalc(4))
