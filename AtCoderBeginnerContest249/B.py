S = input()
sl = S.islower()
su = S.isupper()
if sl or su:
    print('No')
    exit()
for s in S:
    c = S.count(s)
    if c > 1:
        print('No')
        exit()
print('Yes')