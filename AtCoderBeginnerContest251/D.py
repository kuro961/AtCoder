print(297)
A = [i for i in range(1,100)]
A.extend([100 * i for i in range(1,100)])
A.extend([10000 * i for i in range(1,100)])
print(' '.join(map(str, A)))