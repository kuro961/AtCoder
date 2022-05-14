N, Q = map(int, input().split())
num_ind = [i for i in range(N+1)]
ind_num = [i for i in range(N+1)]
for _ in range(Q):
    x = int(input())
    i = num_ind[x]
    if i == N:
        l_num = ind_num[i-1]
        tmp = ind_num[i]
        ind_num[i] = ind_num[i-1]
        ind_num[i-1] = tmp
        
        num_ind[x] = i-1
        num_ind[l_num] = i
    else:
        r_num = ind_num[i+1]
        tmp = ind_num[i]
        ind_num[i] = ind_num[i+1]
        ind_num[i+1] = tmp
        
        num_ind[x] = i+1
        num_ind[r_num] = i
ind_num.pop(0)
print(' '.join(list(map(str, ind_num))))