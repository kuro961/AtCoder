N = int(input())
S = []
for _ in range(N):
    S.append(input())

mp = {}
for i in range(N):
    if S[i] in mp:
        print(f"{S[i]}({mp[S[i]]})")
        mp[S[i]] += 1
    else:
        print(S[i])
        mp[S[i]] = 1
