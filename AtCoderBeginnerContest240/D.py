N = int(input())
A = list(map(int, input().split()))

cnt = 0
pipe = []
for i in range(N):
    cnt += 1
    if pipe:
        if pipe[-1][0] != A[i]:
            pipe.append([A[i], 1])
        else:
            if pipe[-1][0] == pipe[-1][1] + 1:
                cnt -= pipe[-1][1] + 1
                pipe.pop()
            else:
                pipe[-1][1] += 1
    else:
        pipe.append([A[i], 1])
    print(cnt)
