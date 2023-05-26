"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""
number = input("Введите трехзначное число: ")
summa = int(number[0]) + int(number[1]) + int(number[2])
print(f"Сумма цифр числа {number} равна {summa}")

"""
Задача 4: 
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали 
одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем 
Петя и Сережа вместе?

*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""
s = int(input("вводим количество журавликов:"))

katya = (s // 3) * 2
boy = (s - katya) // 2

print("Петя сделал", boy)
print("Катя сделала", katya)
print("Сережа сделал", boy)

"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы 
расплачивались за проезд и получали билет с номером. Счастливым билетом называют 
такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних 
трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется 
написать программу, которая проверяет счастливость билета.

*Пример:*

385916 -> yes
123456 -> no
"""
number = input("Введите номер билета: ") 

if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
    print(number, "-> yes")
else:
    print(number, "-> no")

number = input("Введите номер билета: ") # ввод номера билета

"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k 
долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить 
шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
n, m, k = map(int, input().split())

if k <= n * m and (k % n == 0 or k % m == 0):
    print("yes")
else:
    print("no")
