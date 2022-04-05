"""
УСЛОВИЯ ЗАДАЧИ:
есть 2 точки. Нужно найти расстояние между ними

Теорема Пифагора - гипотенуза =  (Ox)^2 + (Oy)^2 в корне квадратном
1. Нужно найти точку С.
2. Нужно найти отрезок АС. Отрезок АС = xB - xA
3. Нужно найти отрезок АB. Отрезок АB = yB - yA
"""
import math


def my_distance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)


def between_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)


choice = int(input('1 - расстояние до точки. 2 - расстояние между точками'))
if choice == 1:
    x = float(input('Введите координату икс: '))
    y = float(input('Введите координату игрек: '))
    my_distance(x, y)
elif choice == 2:
    x1 = float(input('Введите координату икс первой точки: '))
    y1 = float(input('Введите координату игрек первой точки: '))
    x2 = float(input('Введите координату икс второй точки: '))
    y2 = float(input('Введите координату игрек второй точки: '))
    between_distance(x1, y1, x2, y2)
else:
    print("Ошибка ввода")
