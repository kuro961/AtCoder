N, K = map(int, input().split())
S = input()

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def solve(S_list, num_c):
    c_num = [[0] * 26 for _ in range(num_c)]
    base = ''
    for i in range(num_c):
        for s in S_list:
            tmp = ord(s[i]) - 97
            c_num[i][tmp] += 1
    base = ''
    for cn in c_num:
        tmp = max(cn)
        max_index = cn.index(tmp)
        base += chr(max_index + 97)
    change_num = 0
    for s in S_list:
        for a, b in zip(base, s):
            if a != b:
                change_num += 1
    return change_num
        
divs = make_divisors(N)
ans = N
for d in divs:
    S_list = [S[i*d:(i+1)*d] for i in range(N//d)]
    # print(f'S_list: {S_list}')
    change_num = solve(S_list, d)
    # print(d, change_num)
    if change_num <= K:
        ans = d
        break
print(ans)