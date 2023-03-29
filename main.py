# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = []

for i in range(n):
    element = a1 + i * d
    progression.append(element)

print(progression)


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes


lst = [1, 5, 8, 3, 10, 15, 7]
min_val = 5
max_val = 10
result = find_indexes(lst, min_val, max_val)
print(result)
