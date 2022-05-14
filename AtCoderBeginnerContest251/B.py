N, W = map(int, input().split())
A = list(map(int, input().split()))
import itertools
ans = []
for i in range(1, 4):
    for p in itertools.combinations(A, i):
        sum_p = sum(p)
        if sum_p <= W:
            ans.append(sum_p)
print(len(set(ans)))