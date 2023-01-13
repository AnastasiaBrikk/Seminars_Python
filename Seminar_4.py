# 1) str.split() - метод разделяющий строку на список из строк

# text = 'Privet sosed sdelay omlet'

# print(text.split()) # - ['Privet', 'sosed', 'sdelay', 'omlet']

# 2) randint() - метод генерации рандомного целого числа

# from random import randint

# print(randint(0, 9))

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя
# используйте пробел.Без min() и max() и без sort().

# string = str(input('Введите набор чисел через пробел: ')).split()
# max_number = 0
# min_number = 0
# if string == 0:
#     print('Empty string')
# else:
#     for i in string:
#         i = int(i)
#         if i > max_number:
#             max_number = i
#         if i < min_number:
#             min_number = i
# print(f'Минимальное число: {min_number}, максимальное число: {max_number}')
    

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 с помощью математических формул нахождения корней квадратного уравнения

# A = int(input('Введите значение A не равного нулю: '))
# B = int(input('Введите значение B: '))
# C = int(input('Введите значение C: '))

# def D(a, b, c):
#     if a != 0:
#         discr = b**2 - 4*a*c 
#     return discr

# dis = D(A, B, C)

# if dis > 0:
#     x1 = (-B - dis**0.5)/2*A
#     x2 = (-B + dis**0.5)/2*A
#     print(f'x1 = {round(x1, 1)}, x2 = {round(x2, 1)}')
# elif dis == 0:
#     x = -B/ 2*A
#     print(f'х = {round(x, 1)}')
# else:
#     print('Корней уравнения нет!')



# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
# 3 5
# 15
# a, b = int(input()), int(input())
# def NOK(a, b):
#     import math
#     return (a * b) // math.gcd(a, b)  # функция для нахождения наибольшего общего делителя в модуле math.gcd()

# print(f'Наименьшее общее кратное чисел {a} и {b} = {NOK(a, b)}')


