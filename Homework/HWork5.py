# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b//2) * power(a, b//2)
    else:
        return power(a, b-1) * a

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
result = power(a, b)
print(result)

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return sum(a-1, b) + 1 if a > b else sum(a, b-1) + 1
a = int(input("Enter number A: ")) 
b = int(input("Enter number B: ")) 
print(sum(a,b)) 
   