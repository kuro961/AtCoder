import math


def solve(no_hold, holds):
    min = float("inf")
    for hold in holds:
        tmp = math.sqrt(((no_hold[0] - hold[0]) ** 2) + (((no_hold[1] - hold[1])) ** 2))
        if tmp < min:
            min = tmp
    return min


N, K = map(int, input().split())
A = list(map(int, input().split()))

holds = []
no_holds = []
for n in range(N):
    x, y = map(float, input().split())
    if n + 1 in A:
        holds.append([x, y])
    else:
        no_holds.append([x, y])

ans = 0
for no_hold in no_holds:
    tmp = solve(no_hold, holds)
    if ans < tmp:
        ans = tmp

print(ans)
