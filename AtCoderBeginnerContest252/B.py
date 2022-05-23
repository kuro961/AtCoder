N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_i = [(i + 1) for i, a in enumerate(A) if a == max(A)]
for i in max_i:
    if i in B:
        print('Yes')
        exit()
print('No')