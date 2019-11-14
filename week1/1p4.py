"""
Expression                       Dominant Terms         O(...)

5 + 0.001n^3 + 0.025n            0,001n^3               O(n^3)
500n + 100n^1.5 + 50n*log(n)     100n^1.5+50n*log(n)    O(n^1.5+nlog(n)) == (log n!?)
0.3n + 5n^1.5 + 2.5*1.75n        5n^1.5                 O(n^1.5)
n^2log(n) + n(log(n))^2          nlog(n)^2              O(log(n)) ??
nlog(n) + nlog(n)                nlog(n)                O(log(n))
100n + 0.01n^2                   0.001n^2               O(n^2)
0.01n + 100n^2                   100n^2                 O(n^2)
2n + n^0.5 + 0.5n^1.25           0.5n^1.25              O(n^1.25) //Wortel niet belangrijk

"""