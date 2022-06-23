X, A, D, N = map(int, input().split())
if D != 0:
    n = int((X - A) / D + 1)
else:
    print(abs(X - A))
    exit()

if N < n:
    print(abs(X - (A + (N - 1) * D)))
    exit()

if n < 0:
    print(abs(X - A))
    exit()

S_n = A + (n - 1) * D
S_n1 = A + n * D
if abs((X - S_n)) < abs((S_n1 - X)):
    print(abs(X - S_n))
else:
    print(abs(S_n1 - X))
