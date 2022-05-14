N, A, B = map(int, input().split())
 
S = []
for i in range(N * A):
    if i == 0:
        iro = '.'
    elif i % A == 0:
        if S[i-1][0] == '.':
            iro = '#'
        else:
            iro = '.'
    else:
        iro = S[i-1][0]
    s = []
    for j in range(N * B):
        if j % B == 0 and j != 0:
            if iro == '.':
                iro = '#'
            else:
                iro = '.'
        s.append(iro)
    S.append(''.join(s))
print('\n'.join(S))