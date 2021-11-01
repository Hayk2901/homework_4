b = input()
n = int(input())
if n >= 0:
    print(n * b)
else:
    k = len(b) // (-n)
    if k * (-n) != len(b):
        print("undefinded")
    else:
        for i in range(0, len(b) - k + 1, k):
            # print(b[i:i+k], b[0:k])
            if b[i:i+k] == b[0:k]:
                # print(i, len(b) - k)
                if i == len(b) - k:
                    print(b[0:k])
            else:
                print("undefined")
                break
