"""students = ['Ivan', 'Masha', 'Sasha']
students += ['Olga']
students += 'Olga'
print(students)"""

# Для каждого i выводим сумму соседних
"""
#x = ['1', '2', '3']
x = input().split()
j = 0
i = 0
result = []
if len(x) == 1:
    print(x[0])
else:
    for i in range(len(x)):
        j = 0
        if i == len(x) - 1:
            j = int(x[0]) + int(x[i - 1])
        else:
            j = int(x[i - 1]) + int(x[i + 1])
        result += [j]
        print(result[i], end=' ')
"""
# Вывод только имеющих дубликаты 1 раз
"""#x = ['1', '1', '2', '2', '3', '3']
x = input().split()
x.sort()
i = 0
while i < len(x):
    if x.count(x[i]) > 1:
        print(x[i], end='  ')
        i += x.count(x[i])
    else:
        i += 1"""
# Генерация 2-3 мерных списков
"""n = 3
a = [[0] * n for i in range(n)]
a[0][0] = 5
print(a)"""
a = [[int(i) for i in input().split()]]
b = input()
while b != 'end':
    a.append([int(i) for i in b.split()])
    b = input()
print(a)