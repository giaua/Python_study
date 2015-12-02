# Реализация min()
"""x = [int(i) for i in input().split()]
s = x[0]
for k in x:
    if s > k:
        s = k
print(s)"""
# Сапер
"""
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()"""
# break после того как сумма введенных станет 0
"""i = 1
s = 0
result = 0
while i > 0:
    x = int(input())
    s += x
    result += x ** 2
    if s == 0:
        break
print(result)"""
# 1 2 2 3 3 3 4 4 4 4 .....
"""x = int(input())
n = 0
for i in range(x + 1):
    for j in range(i):
        n += 1
        if n <= x:
            print(i, end=' ')"""
# Test pre final test
# 1) Mine input variant
"""a = [['start']]
while a[-1] != ['end']:
    s = [i for i in input().split()]
    a.append(s)
del a[0], a[-1]"""
# 2) Not mine variant, better one I think
a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
n = len(a)
m = len(a[0])
s = [[0 for j in range(m)] for i in range(n)]
#print(s[0])
#print(n)
for i in range(n):
    for j in range(m):
        if i < (n - 1) and j < (m - 1):
            #print('1) i =', i, 'j =', j, sep=' ')
            s[i][j] = int(a[-1 + i][j]) + int(a[1 + i][j]) + int(a[i][-1 + j]) + int(a[i][1 + j])
        elif i == (n - 1) and j == (m - 1):
            #print('2) i =', i, 'j =', j, sep=' ')
            s[i][j] = int(a[0][j]) + int(a[i - 1][j]) + int(a[i][0]) + int(a[i][j - 1])
            #print(s[i][j])
        elif i == (n - 1) and j < (m - 1):
            #print('3) i =', i, 'j =', j, sep=' ')
            s[i][j] = int(a[0][j]) + int(a[i - 1][j]) + int(a[i][-1 + j]) + int(a[i][1 + j])
            #print(s[i][j])
        elif i < (n - 1) and j == (m - 1):
            #print('4) i =', i, 'j =', j, sep=' ')
            s[i][j] = int(a[-1 + i][j]) + int(a[1 + i][j]) + int(a[i][0]) + int(a[i][j - 1])
#print(s)
for i in range(n):
    if i > 0:
        print()
    for j in range(m):
        print(s[i][j], end=' ')
# second test for pre final test
"""
vse = []
x = 1
string = []
while x > 0:
    i = input()
    if i == 'end':
        break
    else:
        i.split()
        string.append(int(i))
print(string)"""
