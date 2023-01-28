# 1) В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# file = open('seminar.txt', 'r')


# result = [int(i) for i in file.read().split()]
# file.close()
# print(result)

# for i in range(1, len(result)):
#     if result[i] - 1 != result[i - 1]:
#         print(result[i] - 1)


# 2) Написать программу, которая будет удалять все слова в которых есть "абв"

# stroka = [i for i in input('Введите слова через пробел: ').split()]
# result = [i for i in stroka if 'абв' not in i]

# print(*result)
