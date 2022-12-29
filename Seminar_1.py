#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# print('Input a first number')
# a = int(input())
# print('Input a second number')
# b = int(input())

# print(a ** 2 == b or b ** 2 == a)


#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# print('Input five rendom numbers')
# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print(f'Max number is: {max(a, b, c, d, e)}')

# Найти сумму цифр трёхзначного числа
# print('Input a three-digit number:')
# num = int(input())
# print((num % 100 // 10) + (num % 10) + (num // 100))

#3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = abs(input()) - модуль числа
# for i in range(-n, n+1):
#     print(i)


#4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# n = float(input())
# f = int(n)
# print(int((n - f) * 10))
