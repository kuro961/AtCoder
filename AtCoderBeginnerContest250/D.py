M = 10**6
 
N = int(input())
is_prime = [True] * M
is_prime[0] = is_prime[1] = False
# 素数のリスト作成
for i in range(M):
    if is_prime[i]:
        for j in range(i*2, M, i):
            is_prime[j] = False
# 素数の数のリスト作成      
psum = [0] * M
for i in range(M-1):
    psum[i+1] = psum[i]
    if is_prime[i+1]: 
        psum[i+1] += 1
        
ans = 0
for i in range(M):
    if is_prime[i]:
        now = i ** 3
        ans += psum[min(N//now, i-1)]
print(ans)