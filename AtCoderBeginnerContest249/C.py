N, K = map(int, input().split())
S = []
for _ in range(N):
    s = list(map(lambda s: ord(s), list(input())))
    S.append(s)

d = [0] * 26
ans = 0
import itertools
for n in range(1, N+1):
    for i in itertools.combinations(S, n):
        for j in i:
            for k in j:
                d[k - 97] += 1
        t_ans = 0 
        for l in d:
            if l == K:
                t_ans += 1
        if ans < t_ans:
            ans = t_ans
        d = [0] * 26
print(ans)