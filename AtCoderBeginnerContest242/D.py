def g(s, add):
    return chr(ord("A") + (ord(s) - ord("A") + add) % 3)


def solve(t, k):
    if k == 0:
        return g(S[0], t)

    if t == 0:
        return S[k]

    return g(solve(t - 1, k // 2), k % 2 + 1)


S = input()
Q = int(input())

for _ in range(Q):
    t, k = map(int, input().split())
    print(solve(t, k - 1))
