n = int(input())
res = [[0 for j in range(n)] for i in range(n)]
k = 1
i = 0
j = 0
s = 0
t = 0
while k <= n * n:
    while j + s < n and k <= n * n:
        res[i][j] = k
        k += 1
        j += 1
    i += 1
    j -= 1
    while i + s < n and k <= n * n:
        res[i][j] = k
        k += 1
        i += 1
    s += 1
    i -= 1
    j -= 1
    while j + t >= 0 and k <= n * n:
        res[i][j] = k
        k += 1
        j -= 1
    i -= 1
    j += 1
    while i + t > 0 and k <= n * n:
        res[i][j] = k
        k += 1
        i -= 1
    t -= 1
    i += 1
    j += 1
for i in range(len(res)):
    if i > 0:
        print()
    for j in range(len(res[0])):
        print(res[i][j], end=' ')