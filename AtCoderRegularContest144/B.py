def solve(A, base, a, b):
    small_cnt = 0
    big_cnt = 0
    for ele in A:
        if ele == base:
            pass
        if ele < base:
            small_cnt += -(-(base - ele) // a)
        else:
            big_cnt += (ele - base) // b
    if small_cnt <= big_cnt:
        return True
    return False


N, a, b = map(int, input().split())
A = list(map(int, input().split()))

left = 1
right = int(sum(A) / len(A)) + 1
while right - left > 1:
    mid = (left + right) // 2
    if solve(A, mid, a, b):
        left = mid
    else:
        right = mid

print(left)
