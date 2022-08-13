R, C = map(int, input().split())

left = min(R, 15 - R)
right = max(R, 15 - R)
if left <= C and C <= right:
    if R % 2 == 0:
        print("white")
    else:
        print("black")
else:
    if C % 2 == 0:
        print("white")
    else:
        print("black")
