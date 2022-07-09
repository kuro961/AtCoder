S = input()
T = input()


def new_str(string):
    string += "E"
    new_str = []
    pred = string[0]
    r_num = 1
    for s in string[1:]:
        if s != pred:
            new_str.append((pred, r_num))
            pred = s
            r_num = 1
        else:
            r_num += 1
    return new_str


new_S = new_str(S)
new_T = new_str(T)

if len(new_S) != len(new_T):
    print("No")
    exit()

for s, t in zip(new_S, new_T):
    if s == t:
        continue
    else:
        if s[0] == t[0] and s[1] < t[1] and 2 <= s[1]:
            continue
        else:
            print("No")
            exit()
print("Yes")
