Words = input().split('"')
n = len(Words)
s1 = []
s2 = []

for i in range(1, n - 3, 2):
    a = {}
    for j in range(len(Words[i])):
        if Words[-2][j] not in a:
            a[Words[-2][j]] = Words[i][j]
            if len(Words[i]) == 1:
                s1.append(Words[i])
        elif a[Words[-2][j]] == Words[i][j] and j == len(Words[i]) - 1:
            s1.append(Words[i])
        else:
            break
for i in range(1, n - 3, 2):
    a = {}
    for j in range(len(Words[i])):
        if Words[i][j] not in a:
            a[Words[i][j]] = Words[-2][j]
            if len(Words[-2]) == 1:
                s2.append(Words[i])
        elif a[Words[i][j]] == Words[-2][j] and j == len(Words[-2]) - 1:
            s2.append(Words[i])
        else:
            break

print(s1[:min(len(s1), len(s2))])
