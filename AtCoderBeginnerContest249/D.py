N = int(input())
A = list(map(int, input().split()))

Ai = [0] * (2*10**5+1)
m = 0
for a in  A:
    Ai[a] += 1
    m = max(m, a)
    
ans = 0
for k in range(1, m+1):
    for j in range(1, m//k + 1):
        i = k*j
        ans += Ai[k]*Ai[j]*Ai[i]
print(ans)