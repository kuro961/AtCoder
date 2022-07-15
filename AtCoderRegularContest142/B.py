N = int(input())

ans = [0] * N
even_line_start = 1
odd_line_start = N * (N - N // 2) + 1
for i in range(N):
    if (i + 1) % 2 == 0:
        tmp = [j for j in range(odd_line_start, odd_line_start + N)]
        ans[i] = tmp
        odd_line_start += N
    else:
        tmp = [j for j in range(even_line_start, even_line_start + N)]
        ans[i] = tmp
        even_line_start += N

for i in range(N):
    ans[i] = " ".join(map(str, ans[i]))
print("\n".join(ans))
