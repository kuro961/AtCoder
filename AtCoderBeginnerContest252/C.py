N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append([int(i) for i in s])

cand = [0] * 10
for i in range(10):
    reel = [0] * N
    for n in range(N):
        reel[n] = S[n].index(i)
    for n in set(reel):
        c = reel.count(n)
        reel.append(n + 10 * (c - 1))
    cand[i] = max(reel)
print(min(cand))