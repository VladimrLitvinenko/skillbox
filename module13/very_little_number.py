"""Задача 'очень маленькое число' """
"""
- Число Х = 1
- 10000 раз х делится на 2

Выходные данные: 
- Поделенное число
"""

x = 1

for i in range(10000):
    x /= 2
print(x)
