N, X = map(int, input().split())
jump = []
for _ in range(N):
    jump.append(list(map(int, input().split())))

dp = [[False for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
    for j in range(X + 1):
        if dp[i - 1][j]:
            if j + jump[i - 1][0] <= X:
                dp[i][j + jump[i - 1][0]] = True
            if j + jump[i - 1][1] <= X:
                dp[i][j + jump[i - 1][1]] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")
