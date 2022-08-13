import itertools

H1, W1 = map(int, input().split())
A = []
for _ in range(H1):
    row = list(map(int, input().split()))
    A.append(row)
H2, W2 = map(int, input().split())
B = []
for _ in range(H2):
    row = list(map(int, input().split()))
    B.append(row)

idx_h = [i for i in range(H1)]
idx_w = [i for i in range(W1)]
keep_h = list(itertools.combinations(idx_h, H2))
keep_w = list(itertools.combinations(idx_w, W2))
for keep in itertools.product(keep_h, keep_w):
    rm_A = [A[j] for j in keep[0]]
    rm_A = list(zip(*rm_A))
    rm_A = [rm_A[j] for j in keep[1]]
    rm_A = list(zip(*rm_A))

    flag = True
    for j in range(H2):
        for k in range(W2):
            if rm_A[j][k] != B[j][k]:
                flag = False
        if not flag:
            break

    if flag:
        print("Yes")
        exit()

print("No")
