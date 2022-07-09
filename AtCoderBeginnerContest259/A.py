N, M, X, T, D = map(int, input().split())

if X <= M:
    print(T)
else:
    print(T - D * (X - M))
