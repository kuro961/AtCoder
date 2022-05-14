H, W = map(int, input().split())
R, C = map(int, input().split())
 
ans = 0
if 0 < R - 1 <= H:
    ans += 1
if 0 < R + 1 <= H:
    ans += 1
if 0 < C - 1 <= W:
    ans += 1
if 0 < C + 1 <= W:
    ans += 1
print(ans)