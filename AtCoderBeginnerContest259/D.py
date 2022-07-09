import sys

sys.setrecursionlimit(10 ** 6)


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = {}
        for i in range(n):
            self.parent[i] = i

    def root(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return True
        return False

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if root_x != root_y:
            self.parent[root_x] = root_y


N = int(input())
sx, sy, tx, ty = map(int, input().split())

tree = UnionFind(N)
C = []
s_num = []
t_num = []
for i in range(N):
    x, y, r = map(int, input().split())
    C.append((x, y, r))

    d = (x - sx) ** 2 + (y - sy) ** 2
    if d == r ** 2:
        s_num.append(i)

    d = (x - tx) ** 2 + (y - ty) ** 2
    if d == r ** 2:
        t_num.append(i)

for i, c1 in enumerate(C[: len(C) - 1]):
    for j, c2 in enumerate(C[i + 1 :]):
        # print(i, c1, i + j + 1, c2)
        d = (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2
        if d < (c1[2] + c2[2]) ** 2 and (c1[2] - c2[2]) ** 2 < d:
            tree.unite(i, i + j + 1)
        else:
            if d == (c1[2] + c2[2]) ** 2 or (c1[2] - c2[2]) ** 2 == d:
                tree.unite(i, i + j + 1)

for s in s_num:
    for t in t_num:
        if tree.same(s, t):
            print("Yes")
            exit()
print("No")
