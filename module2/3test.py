string = input()
string2 = string[1:]
i = 0
j = 0
while i < len(string):
    s = 1
    j = i
    if j < len(string2):
        while string[i] == string2[j]:
            s += 1
            j += 1
            if j >= len(string2):
                break
    print(string[i], s, sep='', end='')
    i += s