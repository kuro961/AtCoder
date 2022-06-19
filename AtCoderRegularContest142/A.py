def get_rev_K(K):
    str_k = str(K)
    rev_str_k = str_k[::-1]
    return int(rev_str_k)


N, K = map(int, input().split())

rev_K = get_rev_K(K)

if rev_K < K:
    print(0)
    exit()

if K == rev_K:
    tmp = int(N / K)
    ans = len(str(tmp)) - 1
    if K <= N:
        ans += 1
    print(ans)
    exit()

ans = 0
tmp = int(N / K)
ans += len(str(tmp)) - 1
tmp = int(N / rev_K)
ans += len(str(tmp)) - 1
if K <= N:
    ans += 1
if rev_K <= N:
    ans += 1
print(ans)
