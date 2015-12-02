"""
n = int(input())
for i in range(n):
    print('*' * n)
print()
for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
    """
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('\t', end='')
for k in range(c,(d+1)):
    print(k, end='\t')
print()
for i in range(a,(b+1)):
    print(i, end='\t')
    for j in range(c,(d+1)):
        print(j * i, end='\t')
    print()'''
"""
"""
a = int(input())
b = int(input())
s = 0
k = 0
while a % 3 != 0:
    a += 1
for i in range(a, b + 1, 3):
    s += i
    k += 1
print(s / k)
"""
"""
string_nucl = input()
gcount = (string_nucl.upper()).count('G')
ccount = (string_nucl.upper()).count('C')
print(((gcount + ccount) / len(string_nucl)) * 100)
"""
string = input()
i = 0
while i < len(string):
    s = 1
    j = i + 1
    while string[j] == string[i]:
        s += 1
        j += 1
        if j == len(string):
            break
    print(string[i], s, sep='', end='')
    i += s
    if i + 1 == len(string):
        print(string[i], 1, sep='', end='')
        break