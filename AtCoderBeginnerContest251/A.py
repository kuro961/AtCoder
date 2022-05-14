S = input()
ans = S
for _ in range(1, 6 // len(S)):
    ans += S
print(ans)