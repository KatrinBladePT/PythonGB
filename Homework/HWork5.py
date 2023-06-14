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
