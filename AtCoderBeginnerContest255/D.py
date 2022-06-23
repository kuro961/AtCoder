import bisect

N, Q = map(int, input().split())
A = list(sorted(map(int, input().split())))

sum_A = [0] * (N + 1)
for i in range(N):
    sum_A[i + 1] = sum_A[i] + A[i]

for q in range(Q):
    X = int(input())
    idx = bisect.bisect_left(A, X)
    ans = X * idx - sum_A[idx] + sum_A[N] - sum_A[idx] - X * (N - idx)
    print(ans)
