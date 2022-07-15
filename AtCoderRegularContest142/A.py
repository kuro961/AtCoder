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
    ans = 0
    tmp = int(N / K)
    if 0 < tmp:
        ans += len(str(tmp))
    print(ans)
    exit()

ans = 0
tmp = int(N / K)
if 0 < tmp:
    ans += len(str(tmp))

tmp = int(N / rev_K)
if 0 < tmp:
    ans += len(str(tmp))

print(ans)
