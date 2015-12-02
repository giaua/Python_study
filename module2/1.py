a = int(input())
b = int(input())
s = a
i = 1
while i != 0:
    if s % a == 0 and s % b == 0:
        i = 0
    else:
        s += 1
print(s)