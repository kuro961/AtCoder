def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


def solve(N, str_N, r_num):
    if int(str_N * r_num) <= N:
        return int(str_N * r_num)
    if str_N == "1":
        return int("9" * (r_num - 1))
    return int(str(int(str_N) - 1) * r_num)


def get_ans(N):
    str_N = str(N)
    divs = make_divisors(len(str_N))
    divs.remove(len(str_N))
    ans = 0
    for d in divs:
        tmp = solve(N, str_N[:d], int(len(str_N) / d))
        if tmp > ans:
            ans = tmp
    return ans


T = int(input())
for _ in range(T):
    N = int(input())
    ans = get_ans(N)
    print(ans)
