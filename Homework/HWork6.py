# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = []  
for i in range(n):
    an = a1 + i * d  
    progression.append(an)  

print(progression) 

# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного минимума 
# и не больше заданного максимума)

def find_indexes(lst, min_val, max_val):
    result = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            result.append(i)
    return result

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_val = 3
max_val = 7
indexes = find_indexes(lst, min_val, max_val)
print(indexes)

# another example

def find_indexes2(lst2, min_val2, max_val2):
    return [i for i, x in enumerate(lst2) if min_val2 <= x <= max_val2]

lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min_val2 = 3
max_val2 = 7
indexes2 = find_indexes2(lst2, min_val2, max_val2)
print(indexes2)


