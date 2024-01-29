# Домашнее задание №1

# a = 11
# b = 23
# print("a:", a)
# print("b:", b)
#
# a = a + b
# b = a - b
# a = a - b
#
# print("a:", a)
# print("b:", b)



# Домашнее задание №2

# n = int(input("Введите количество копеек от 1 до 99: "))
# if 1 <= n <= 99:
#     if n == 11 or n == 12 or n == 13 or n == 14:
#         print(n, "копеек")
#     else:
#         if n % 10 == 1:
#             print(n, "копейка")
#         if n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
#             print(n, "копейки")
#         if 5 <= n % 10 <= 9 or n % 10 == 0:
#             print(n, "копеек")
# else:
#     print("Ошибка диапазона 1-99")



# Домашнее задание №3

# qty = int(input("Укажите кол-во символов: "))
# vid = input("Укажите тип символов: ")
# orient = int(input("Укажите ориентацию линии 0 или 1: "))
# while qty:
#     if orient == 0:
#         print(vid, end=" ")
#         qty -= 1
#     elif orient == 1:
#         print(vid)
#         qty -= 1



# Домашнее задание №4

# a = [float(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
# print("Количество чисел: ", len(a))
# sra = sum(a) / len(a)
# print("Среднее арифметическое: ", sra)
# print("Минимальное число: ", min(a))
# print("Максимальное число: ", max(a))



# Домашнее задание №5

# qty = int(input("Кол-во элементов списка: "))
# lst = []
# for i in range(qty):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         lst.append(x)
#     else:
#             print(x,"Не делится на 3 без остатка.")
# print(lst)


# Домашнее задание №6

ch = [int(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
k = int(input("Введите индекс: " '\n' "k = "))
c = int(input("Введите число, которое хотите добавить: " '\n' "c = "))
ch.insert(k, c)
print(ch)



# Домашнее задание №7