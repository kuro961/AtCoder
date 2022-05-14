N = int(input())
o_dict = {}
oi_dict = {}
for i in range(N):
    S, T = input().split()
    if S in o_dict:
        pass
    else:
        o_dict[S] = int(T)
        oi_dict[S] = i + 1
ans = max(o_dict.items(), key=lambda x: x[1])   
print(oi_dict[ans[0]])