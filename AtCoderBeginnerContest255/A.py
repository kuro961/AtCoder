R, C = map(int, input().split())
A = []
for i in range(2):
    a = list(map(int, input().split()))
    A.append(a)
print(A[R - 1][C - 1])
