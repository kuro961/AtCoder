from collections import deque

s = input()

q = deque()
q.append(s)
mp = {s: 0}
while True:
    current = q.popleft()
    if current == "atcoder":
        print(mp[current])
        exit()

    for i in range(6):
        next = list(current)
        next[i] = current[i + 1]
        next[i + 1] = current[i]
        next = "".join(next)
        if next not in mp.keys():
            q.append(next)
            mp[next] = mp[current] + 1
