N = int(input())
table = []
for _ in range(N):
    x = input()
    table.append(x)

for i in range(N):
    for j in range(i + 1, N):
        if table[i][j] == "D":
            if table[j][i] != "D":
                print("incorrect")
                exit()
        if table[i][j] == "W":
            if table[j][i] != "L":
                print("incorrect")
                exit()
        if table[i][j] == "L":
            if table[j][i] != "W":
                print("incorrect")
                exit()
print("correct")
