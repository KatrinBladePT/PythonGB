# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве 
# A[1..N]. Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя 
# строка содержит число X
n = int(input("Enter list size: "))
print("size:", n)
a = list(map(int, input("Enter list: ").split()))
print("list:", a)
x = int(input("Enter number: "))
print("number:", x)
count = a.count(x)

print(count)
