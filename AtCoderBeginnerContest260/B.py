def solve(score, ans, max_num):
    sort_idx = [i[0] for i in sorted(enumerate(score), key=lambda x: x[1], reverse=True)]
    cnt = 0
    for i in sort_idx:
        if max_num <= cnt:
            break
        if i not in ans:
            cnt += 1
            ans.append(i)
    return ans


N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = [a + b for a, b in zip(A, B)]

ans = []
ans = solve(A, ans, X)
ans = solve(B, ans, Y)
ans = solve(C, ans, Z)
ans.sort()
ans = [str(a + 1) for a in ans]
print("\n".join(ans))
