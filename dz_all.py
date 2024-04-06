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
# 
# class Car:
#
#     def __init__(self, model_name, year_of_release, manufacturer, engine_power, colour, price):
#         self.model_name = model_name
#         self.year_of_release = year_of_release
#         self.manufacturer = manufacturer
#         self.engine_power = engine_power
#         self.colour = colour
#         self.price = price
#
#     def printer(self):
#         print(self.model_name)
#         print(self.year_of_release)
#         print(self.manufacturer)
#         print(self.engine_power)
#         print(self.colour)
#         print(self.price)
#
#
# def __init__(self, model_name, year_of_release, manufacturer, engine_power, colour, price):
#     def set_model_name(self, model_name):
#         self.model_name = model_name
#
#     def get_model_name(self):
#         return self.model_name
#
#     def set_year_of_release(self, year_of_release):
#         self.year_of_release = year_of_release
#
#     def get_year_of_release(self):
#         return self.year_of_release
#
#
# if __name__ == '__main__':
#     auto = Car("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
#     auto.printer()


# Домашнее задание №23

# class Person:
#     def __init__(self, name: str, old: float) -> None:
#         self.__name = name
#         self.__old = old
#
#     @staticmethod
#     def __check_value(value, types) -> bool:
#         return isinstance(value, types)
#
#     @property
#     def old(self) -> float:
#         return self.__old
#
#     @old.setter
#     def old(self, value: float) -> None:
#         if self.__check_value(value, (int, float)):
#             self.__old = value
#
#     @old.deleter
#     def old(self) -> None:
#         del self.__old
#
#     @property
#     def name(self) -> str:
#         return self.__name
#
#     @name.setter
#     def name(self, value: str) -> None:
#         if self.__check_value(value, str):
#             self.__name = value
#
#     @name.deleter
#     def name(self) -> None:
#         del self.__name
#
#
# pers1 = Person("Irina", 26)
# print(pers1.__dict__)
# pers1.name = "Igor"
# pers1.old = 31
# print(pers1.name)
# print(pers1.old)
# pers1.old = 26
# del pers1.name
# print(pers1.__dict__)


# Домашнее задание №24
#
# class AreaCalculator:
#     # Счетчики количества вызовов методов
#     triangle_count: int = 0
#     rectangle_count: int = 0
#     square_count: int = 0
#
#     @staticmethod
#     def calculate_triangle_area(a: float, b: float, c: float = None, method: str = 'основание_высота') -> float:
#         """
#         Вычисляет площадь треугольника.
#         """
#         # Увеличиваем счетчик вызовов метода для треугольника
#         AreaCalculator.triangle_count += 1
#         if method == 'основание_высота':
#             if c is not None:
#                 raise ValueError("Для метода 'основание_высота' не должно быть передано третье значение")
#             # Вычисляем площадь треугольника через основание и высоту
#             return 0.5 * a * b
#         elif method == 'Герон':
#             if c is None:
#                 raise ValueError("Для метода 'Герон' должно быть передано три значения")
#             # Вычисляем полупериметр
#             semi_perimeter = (a + b + c) / 2
#             # Вычисляем площадь треугольника по формуле Герона
#             return (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5
#         else:
#             raise ValueError("Неверный метод для вычисления площади треугольника")
#
#     @staticmethod
#     def calculate_rectangle_area(length: float, width: float) -> float:
#         """
#         Вычисляет площадь прямоугольника.
#         """
#         # Увеличиваем счетчик вызовов метода для прямоугольника
#         AreaCalculator.rectangle_count += 1
#         # Вычисляем площадь прямоугольника
#         return length * width
#
#     @staticmethod
#     def calculate_square_area(side: float) -> float:
#         """
#         Вычисляет площадь квадрата.
#         """
#         # Увеличиваем счетчик вызовов метода для квадрата
#         AreaCalculator.square_count += 1
#         # Вычисляем площадь квадрата
#         return side ** 2
#
#     @staticmethod
#     def get_total_count() -> int:
#         """
#         Получает общее количество вызовов всех методов.
#         """
#         # Возвращает общее количество вызовов всех методов
#         return AreaCalculator.triangle_count + AreaCalculator.rectangle_count + AreaCalculator.square_count
#
#
# # Пример использования:
# triangle_area_heron = AreaCalculator.calculate_triangle_area(3, 4, 5, method='Герон')
# print(f"Площадь треугольника по формуле Герона (3, 4, 5): {triangle_area_heron}")
#
# triangle_area_base_height = AreaCalculator.calculate_triangle_area(6, 7, method='основание_высота')
# print(f"Площадь треугольника через основание и высоту (6, 7): {triangle_area_base_height}")
#
# square_area = AreaCalculator.calculate_square_area(7)
# print(f"Площадь квадрата (7): {square_area}")
#
# rectangle_area = AreaCalculator.calculate_rectangle_area(2, 6)
# print(f"Площадь прямоугольника (2, 6): {rectangle_area}")
#
# print("Количество подсчетов площади:", AreaCalculator.get_total_count())


# Домашнее задание №25

# import math
#
#
# class Pair:
#     def __init__(self, a: float, b: float):
#         self.A = a  # Первый катет
#         self.B = b  # Второй катет
#
#     def change_numbers(self, a: float, b: float) -> None:
#         """Метод для изменения значений катетов A и B."""
#         self.A = a
#         self.B = b
#
#     def product(self) -> float:
#         """Метод для вычисления произведения катетов A и B."""
#         return self.A * self.B
#
#     def sum(self) -> float:
#         """Метод для вычисления суммы катетов A и B."""
#         return self.A + self.B
#
#
# class RightTriangle(Pair):
#     def __init__(self, a: float, b: float):
#         super().__init__(a, b)
#
#     def hypotenuse(self) -> float:
#         """Метод для вычисления длины первой гипотенузы прямоугольного треугольника."""
#         return math.sqrt(self.A ** 2 + self.B ** 2)
#
#     def second_hypotenuse(self) -> float:
#         """Метод для вычисления длины второй гипотенузы прямоугольного треугольника."""
#         return math.sqrt(self.A ** 2 + self.B ** 2 + (2 * self.A * self.B))
#
#     def area(self) -> float:
#         """Метод для вычисления площади прямоугольного треугольника."""
#         return 0.5 * self.A * self.B
#
#
# # Пример использования классов
# pair1 = Pair(5, 8)
# triangle1 = RightTriangle(pair1.A, pair1.B)
#
# # Вывод информации о прямоугольном треугольнике
# print("Гипотенуза △ABC:", "{:.2f}".format(triangle1.hypotenuse()))
# print("Прямоугольный треугольник △ABC ({}, {}, {:.2f})".format(triangle1.A, triangle1.B, triangle1.hypotenuse()))
# print("Площадь △ABC:", "{:.1f}".format(triangle1.area()))
# print()
# print("Сумма:", pair1.sum())
# print("Произведение:", pair1.product())
# print()
#
# pair2 = Pair(15, 20)
# triangle2 = RightTriangle(pair2.A, pair2.B)
#
# # Вывод информации о прямоугольном треугольнике
# print("Гипотенуза △ABC:", "{:.2f}".format(triangle2.hypotenuse()))
# print("Гипотенуза △ABC:", "{:.2f}".format(triangle2.second_hypotenuse()))
# print("Сумма:", pair2.sum())
# print("Произведение:", pair2.product())
# print("Площадь △ABC:", "{:.1f}".format(triangle2.area()))
# print()


# Домашнее задание №26
#
# class Student:
#     """Класс, представляющий студента."""
#
#     def __init__(self, name: str, laptop: 'Laptop'):
#         """Инициализирует объект студента."""
#         self.name = name
#         self.laptop = laptop
#
#     def __str__(self) -> str:
#         """Возвращает строковое представление объекта студента."""
#         return f"{self.name} => {self.laptop.model}, {self.laptop.processor}, {self.laptop.memory}"
#
#     class Laptop:
#         """Класс, представляющий ноутбук."""
#
#         def __init__(self, model: str, processor: str, memory: int):
#             """Инициализирует объект ноутбука."""
#             self.model = model
#             self.processor = processor
#             self.memory = memory
#
#
# laptop1 = Student.Laptop("HP", "i7", 16)
# student1 = Student("Roman", laptop1)
#
# laptop2 = Student.Laptop("HP", "i7", 16)
# student2 = Student("Vladimir", laptop2)
#
# print(student1)
# print(student2)


# Домашнее задание №27
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError("Секунды должны быть целым числом")
#         self.seconds = seconds % self.__DAY
#
#     def get_format_time(self):
#         s = self.seconds % 60
#         m = (self.seconds // 60) % 60
#         h = (self.seconds // 3600) % 24
#         return f"{Clock.__get_formatted_num(h)}:{Clock.__get_formatted_num(m)}:{Clock.__get_formatted_num(s)}"
#
#     @staticmethod
#     def __get_formatted_num(num):
#         return str(num) if num > 9 else f"0{num}"
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return Clock(self.seconds + other.seconds)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.seconds == other.seconds
#
#     def __ne__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         return self.seconds != other.seconds
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return Clock((self.seconds - other.seconds) % self.__DAY)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return Clock((self.seconds * other.seconds) % self.__DAY)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return Clock((self.seconds // other.seconds) % self.__DAY)
#
#     def __mod__(self, other: 'Clock') -> 'Clock':
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return Clock((self.seconds % other.seconds) % self.__DAY)
#
#     def __iadd__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         self.seconds += other.seconds
#         self.seconds %= self.__DAY
#         return self
#
#     def __isub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом Clock")
#         self.seconds -= other.seconds
#         self.seconds %= self.__DAY
#         return self
#
#     def __imul__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         self.seconds *= other.seconds
#         self.seconds %= self.__DAY
#         return self
#
#     def __ifloordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         self.seconds //= other.seconds
#         self.seconds %= self.__DAY
#         return self
#
#     def __imod__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         self.seconds %= other.seconds
#         self.seconds %= self.__DAY
#         return self
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return self.seconds < other.seconds
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return self.seconds <= other.seconds
#
#     def __gt__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return self.seconds > other.seconds
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise TypeError("Правый операнд должен быть типом Clock")
#         return self.seconds >= other.seconds
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
#
# # Результаты операций
# print("Сложение:", (c1 + c2).get_format_time())
# print("Вычитание:", (c1 - c2).get_format_time())
# print("Умножение:", (c1 * c2).get_format_time())
# print("Целочисленное деление:", (c1 // c2).get_format_time())
# print("Остаток от деления:", (c1 % c2).get_format_time())
#
# # Изменение текущего объекта
# c1 += c2
# print("Изменение текущего объекта (сложение):", c1.get_format_time())
# c1 -= c2
# print("Изменение текущего объекта (вычитание):", c1.get_format_time())
# c1 *= c2
# print("Изменение текущего объекта (умножение):", c1.get_format_time())
# c1 //= c2
# print("Изменение текущего объекта (целочисленное деление):", c1.get_format_time())
# c1 %= c2
# print("Изменение текущего объекта (остаток от деления):", c1.get_format_time())
#
# # Сравнение
# if c1 < c2:
#     print("Первое время меньше второго")
# elif c1 <= c2:
#     print("Первое время меньше или равно второму")
# elif c1 > c2:
#     print("Первое время больше второго")
# elif c1 >= c2:
#     print("Первое время больше или равно второму")


# Домашнее задание №28

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    def __init__(self, color: str) -> None:
        """
        Инициализация фигуры.
        """
        self.color = color

    @abstractmethod
    def perimeter(self) -> float:
        """
        Вычисление периметра фигуры.
        """
        pass

    @abstractmethod
    def area(self) -> float:
        """
        Вычисление площади фигуры.
        """
        pass

    @abstractmethod
    def draw(self) -> None:
        """
        Отрисовка фигуры.
        """
        pass

    @abstractmethod
    def additional_info(self) -> None:
        """
        Дополнительная информация о фигуре.
        """
        pass

    def display_info(self) -> None:
        """
        Вывод информации о фигуре.
        """
        print(f"==={self.__class__.__name__}===")
        self.additional_info()
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()
        print()


class Square(Shape):
    def __init__(self, side_length: float, color: str) -> None:
        """
        Инициализация квадрата.
        """
        super().__init__(color)
        self.side_length = side_length

    def perimeter(self) -> float:
        return 4 * self.side_length

    def area(self) -> float:
        return self.side_length ** 2

    def draw(self) -> None:
        for _ in range(self.side_length):
            print("*" * self.side_length)

    def additional_info(self) -> None:
        print(f"Сторона: {self.side_length}")


class Rectangle(Shape):
    def __init__(self, length: float, width: float, color: str) -> None:
        """
        Инициализация прямоугольника.
        """
        super().__init__(color)
        self.length = length
        self.width = width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def area(self) -> float:
        return self.length * self.width

    def draw(self) -> None:
        for _ in range(self.width):
            print("*" * self.length)

    def additional_info(self) -> None:
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")


class Triangle(Shape):
    def __init__(self, side1: float, side2: float, side3: float, color: str) -> None:
        """
        Инициализация треугольника.
        """
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        return round(self.side1 + self.side2 + self.side3, 1)

    def area(self) -> float:
        s = self.perimeter() / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)

    def draw(self) -> None:
        for i in range(1, 7):
            spaces = " " * (6 - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

    def additional_info(self) -> None:
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")


# Пример:

square = Square(3, "red")
rectangle = Rectangle(7, 3, "green")
triangle = Triangle(11, 6, 6, "yellow")

shapes = [square, rectangle, triangle]

for shape in shapes:
    shape.display_info()


# Домашнее задание №29

