a, b, c, d, e, f, x  = map(int, input().split())

def get_dis(a, b, c, x):
    q = x // (a + c)
    r = x % (a + c)
    return (a * q + min(a, r)) * b

t = get_dis(a, b, c, x)
a = get_dis(d, e, f, x)

if a < t:
    print('Takahashi')
elif t < a:
    print('Aoki')
else:
    print('Draw')