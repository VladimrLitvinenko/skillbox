"""
(OA)= в корне квадратном (Ox)2 + (Oy)2
"""
import math

x = int(input("Введите координаты х: "))
y = int(input("Введите координаты y: "))

distance = math.sqrt(x ** 2 + y ** 2)

print("distance = ", distance)