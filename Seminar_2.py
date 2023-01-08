# 1 Напишите программу, которая принимает на вход число N и выдаёт последовательность размера N из чередующихся по знаку степеней тройки.
#*Пример: Для N = 5: 1, -3, 9, -27, 81

# print('Input an integer number:')
# N = int(input())
# if N == 0:
#     print(3**N)
#     exit()
# for i in range(N):
#     print((-3)**i, end = ' ')


# 2 Напишите программу, в которой пользователь будет задавать две строки, одна из них - буква, а вторая фраза/слово,
# программа должна посчитать сколько раз буква встретилась во второй строке. (Не используя встроенные функции, count)

# letter = input('Input a letter search: ')
# string = str(input('Input a sentence or word: '))
# count = 0
# for i in string:
#     if letter == i:
#         count +=1
# print(count)



# 3 Вводятся сумма двух чисел S и их произведение P
# Написать программу, которая выведет эти числа.

# *Пример*
# Ввод: 5 6
# Вывод: 2 3

# S = int(input('Input a sum of numbers: '))
# P = int(input('Input a product of numbers: '))
# for a in range(S):
#     for b in range(S):
#         if a + b == S and a * b == P:
#             print(a, b)
#             exit()






# 4 Дан список из 5 ростов учеников, и дан ещё один ученик. Необходимо его поставить куда-то. Список идёт по уменьшению.

# list = [150, 148, 148, 145, 144]

# H = 143  #int(input('Input a hight of student: '))

# list.append(H)

# list.sort(reverse=True) #Сортировка в обратном порядке - reverse(descending sort method)

# print(list)
