import math

a, b, d = map(int, input().split())


def getXY(r, degree):
    rad = math.radians(degree)
    x = r * math.cos(rad)
    y = r * math.sin(rad)
    return x, y


def getRD(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    rad = math.atan2(y, x)
    degree = math.degrees(rad)
    return r, degree


r, degree = getRD(a, b)
x, y = getXY(r, degree + d)
print(x, y)
