"""Задача 'Приоритет Задач' """
"""
Условия задачи:
- Даны два числа
- Сравнивается кол-во цифр

Выходные данные:
- Сообщение о том, где больше цифр (либо равно)
"""


def numeral_count(number):
    if number < 0:
        print("Числ негативное. Обнуляеем")
        return 0
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


first_task = int(input('Введите первое число: '))
second_task = int(input('Введите второе число: '))

fist_numeral = numeral_count(first_task)
second_numeral = numeral_count(second_task)

if fist_numeral > second_numeral:
    print('цифр больше в первом числе = ', fist_numeral)
elif fist_numeral < second_numeral:
    print('цифр больше во втором числе = ', second_numeral )