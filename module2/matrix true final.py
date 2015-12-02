a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
s = 0
for i in range(len(a)):
    print()
    for j in range(len(a[0])):
        s = a[-1 + i][j] + a[(1 + i) % len(a)][j] + a[i][-1 + j] + a[i][(1 + j) % len(a[0])]
        print(s, end=' ')
