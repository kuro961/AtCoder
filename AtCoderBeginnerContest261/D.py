N, M = map(int, input().split())
X = list(map(int, input().split()))
bonus = dict.fromkeys([i for i in range(N + 1)], 0)
for _ in range(M):
    c, y = map(int, input().split())
    bonus[c] = y

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = max(dp[i - 1])
        else:
            dp[i][j] = dp[i - 1][j - 1] + X[i - 1] + bonus[j]

print(max(dp[-1]))
