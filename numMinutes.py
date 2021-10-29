logs = input()
k = int(input())
a1 = []
a2 = []
a3 = []
a4 = []
for i in range(k):
    a3.append(0)
z = True
logs = logs.replace("[", "")
logs = logs.replace("]", "")
ll = logs.split(',')
n = len(ll)
for i in range(0, n, 2):
    if [ll[i], ll[i+1]] in a4:
        continue
    a4.append([ll[i], ll[i+1]])
    a1.append(int(ll[i]))
    a2.append(int(ll[i+1]))
n = len(a1)
# print(a1)
# print(a2)
k = 0
a1.sort()
if n == 1:
    a3[0] += 1
else:
    for i in range(n - 1):
        if a1[i] == a1[i+1]:
            k += 1
            if i == n-2:
                a3[k] += 1
        elif i == n-2:
            a3[k] += 1
            a3[0] += 1
        else:
            a3[k] += 1
            k = 0
print(a3)
