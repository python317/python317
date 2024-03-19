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

# ch = [int(input("Введите число: ")) for i in range(int(input("Введите количество чисел последовательности: ")))]
# k = int(input("Введите индекс: " '\n' "k = "))
# c = int(input("Введите число, которое хотите добавить: " '\n' "c = "))
# ch.insert(k, c)
# print(ch)

# Домашнее задание №7

# from math import sqrt, pi
#
# print("1-треугольник, 2-прямоугольник, 3-круг")
# fig = input("Выберите фигуру: ")
# if fig == '1':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %.2f" % s)
# elif fig == '2':
#     print("Длина сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь: %.2f" % (a * b))
# elif fig == '3':
#     r = float(input("Радиус круга R = "))
#     print("Площадь: %.2f" % (pi * r ** 2))10

# else:
#     print("Ошибка ввода")

# Домашнее задание №8

# from math import sqrt, pi
#
# fig = input("1-треугольник, 2-прямоугольник, 3-круг: ")
# def triangle(a, b, c):
#     p = (a + b + c) / 2
#     return sqrt(p * (p - a) * (p - b) * (p - c))
# def rectangle(a, b):
#     return a * b
# def circle(r):
#     return pi * r ** 2
# if fig == '1':
#     AB = float(input("Первая сторона: "))
#     BC = float(input("Вторая сторона: "))
#     CA = float(input("Третья сторона: "))
#     print("Площадь треугольника: %.2f" % triangle(AB, BC, CA))
# elif fig == '2':
#     l = float(input("Длина: "))
#     w = float(input("Ширина: "))
#     print("Площадь прямоугольника: %.2f" % rectangle(l, w))
# elif fig == '3':
#     rad = float(input("Радиус: "))
#     print("Площадь круга: %.2f" % circle(rad))
# else:
#     print("Ошибка ввода")

# Домашнее задание №9

# from random import randint
#
# x = tuple(randint(0, 9) for i in range(10))
# print(x)
# y = []
# for i in x:
#     if i not in y:
#         y.append(i)
# for i in y:
#     print("Количество ", i, "=", x.count(i))

# Домашнее задание №10
#
# print("Ссылка с одной строкой кода для GitHub")

# Домашнее задание №11

# mat = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
# physic = {"Максим", "Матвей", "Александр"}
#
# all = mat | physic
# print(all)
#
# victory = mat & physic
# print(victory)
#
# mat = victory
# print(mat)

# Домашнее задание №12

# sales = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#          'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#          'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#          'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ":", sales[x][y])
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# Елена Анатольевна, учитывая что python учитывает регистр, соответсвенно John не равно john, если возможность
# пользователю вводить данные без учета регистра? Как это сделать?

# Домашнее задание №13

# students = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     student_name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     students[student_name] = point
#     s += point
#     avrg = s / n
#
# print("Средний балл: %.0f. Студенты с баллом выше среднего: " % avrg)
# for i in students:
#     if students[i] > avrg:
#         print(i)


# Домашнее задание №14

# def outer(a,b,c):
#     def inner(i,j):
#         return i*j
#
#     s = 2 * (inner(a,b) + inner(a, c) +inner(b,c))
#     return s
#
# print(outer(2,4,6))
# print(outer(5,8,2))
# print(outer(1,6,8))

# Домашнее задание №15

# print(list(filter(lambda slovo: slovo == slovo[::-1], ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom'))))


# Домашнее задание №16
#
# def avg(fn):
#     def wrap(*arg):
#         a = ""16
#         for i in arg:
#             a += str(i) + ", "  # "2, 3, 3, 4, "
#         print("Среднее арифметическое:", a[:-2], "=", fn(*arg) / len(arg))
#
#     return wrap
#
#
# @avg
# def summa(*args):  # (2, 3, 3, 4)
#     print("Сумма чисел:", ", ".join(map(str, args)), "=", sum(args))
#     return sum(args)
#
#
# summa(2, 3, 3, 4)


# Домашнее задание №17
#
# def fio():
#     names = input("Введите Фамилию, Имя, Отчество: ").split()
#     return f'{names[0]} {names[1][0]}.{names[2][0]}.'.title()
#
#
# print(fio())


# Домашнее задание №18

# import re
#
# s = "+ 7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# pattern = r'\+?7\d{10}'
#
# print(re.findall(pattern, s))


# Домашнее задание №19

# import re
#
# s = "my-p@ssw0rd"
# reg = r"^[a-zA-Z0-9_@-]{6,18}$"
# print(re.findall(reg, s))

# Домашнее задание №20

# def negative_numbers(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negative_numbers(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_numbers(lst))

# Домашнее задание №21
#
# import os
#
#
# root = r'nested1\nested2'
# objs = os.listdir(root)
# print(objs)
#
# print(sorted(objs, reverse=True))


# Домашнее задание №22

class Car:

    def __init__(self, model_name, year_of_release, manufacturer, engine_power, colour, price):
        self.model_name = model_name
        self.year_of_release = year_of_release
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.colour = colour
        self.price = price

    def printer(self):
        print(self.model_name)
        print(self.year_of_release)
        print(self.manufacturer)
        print(self.engine_power)
        print(self.colour)
        print(self.price)


def __init__(self, model_name, year_of_release, manufacturer, engine_power, colour, price):
    def set_model_name(self, model_name):
        self.model_name = model_name

    def get_model_name(self):
        return self.model_name

    def set_year_of_release(self, year_of_release):
        self.year_of_release = year_of_release

    def get_year_of_release(self):
        return self.year_of_release


if __name__ == '__main__':
    auto = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
    auto.printer()


# Домашнее задание №23
