S = input()

ans = ""
for i in range(97, 123):
    c = S.count(chr(i))
    ans += chr(i) * c
print(ans)
