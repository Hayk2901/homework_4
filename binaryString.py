n = int(input())
b = input()
k = 0
qan = 0
for i in range(n-2):
    if k == 0 and b[i] == '0' and b[i+1] == '1' and b[i+2] == '0':
        k += 1
        i += 2
        if i >= n-2:
            qan += 1
            break
    elif k != 0 and b[i] == '1' and b[i+1] == '0':
        k += 1
        i += 1
        if i >= n-2:
            qan += (k+1) // 2
            break
    else:
        qan += (k+1) // 2
        k = 0
print(qan)
