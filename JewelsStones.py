jewels = input()
stones = input()
n = len(jewels)
m = len(stones)
k = 0
for i in range(n):
    for j in range(m):
        if jewels[i] == stones[j]:
            k += 1
print(k)
