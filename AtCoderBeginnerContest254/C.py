N, K = map(int, input().split())
A = list(map(int, input().split()))

# N = 2 * 10 ** 5
# K = 2
# A = [i for i in range(2 * 10 ** 5)]

A_sort = sorted(A)

for i in range(K):
    tmp = [A[i + j * K] for j in range(-(-(N - i) // K))]
    tmp.sort()
    for j, t in enumerate(tmp):
        A[i + j * K] = t

if A == A_sort:
    print("Yes")
else:
    print("No")
