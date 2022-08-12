import bisect

N, K = map(int, input().split())
P = list(map(int, input().split()))

ans = [-1 for _ in range(N + 1)]
table_top_card = []
table_card = []
for i in range(N):
    index = bisect.bisect_left(table_top_card, P[i])

    if index == len(table_card):
        table_top_card.append(P[i])
        table_card.append([P[i]])

        if len(table_card[index]) == K:
            for j in table_card[index]:
                ans[j] = i + 1
            table_card.pop(index)
            table_top_card.pop(index)

    else:
        table_card[index].append(P[i])
        table_top_card[index] = P[i]

        if len(table_card[index]) == K:
            for j in table_card[index]:
                ans[j] = i + 1
            table_card.pop(index)
            table_top_card.pop(index)

ans = list(map(str, ans[1:]))
print("\n".join(ans))
