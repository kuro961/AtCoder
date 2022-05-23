from collections import Counter
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N = int(input())
A = list(map(int, input().split()))

A = Counter(A)
tmp = []
for i in A.values():
    if i >= 2:
        tmp.append(cmb(i, 2) * (N - i))
    if i >= 3:
        tmp.append(cmb(i, 3))
        
print(cmb(N, 3) - sum(tmp))
