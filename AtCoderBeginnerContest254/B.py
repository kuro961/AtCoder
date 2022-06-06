N = int(input())

ans = []
for i in range(N):
    t_ans = []
    for j in range(i + 1):
        if j == 0 or j == i:
            t_ans.append(1)
        else:
            t_ans.append(ans[i - 1][j - 1] + ans[i - 1][j])
    ans.append(t_ans)

for a in ans:
    a = list(map(str, a))
    print(' '.join(a))
