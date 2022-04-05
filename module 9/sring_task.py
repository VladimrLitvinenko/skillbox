print("***** TASK 1 *****")
"""Задача на посчет определенных символов в тексте"""

# text = input("Введите текст: ")
# first_sym = input("Введите первую букву: ")
# second_sym = input("Введите вторую букву: ")
# first_sym_count = 0
# second_sym_count = 0
# for symbol in text:
#     if symbol == first_sym:
#         first_sym_count += 1
#     if symbol == second_sym:
#         second_sym_count += 1
# print(f"кол-во символа {first_sym} в тексте {text} = {first_sym_count}")
# print(f"кол-во символа {second_sym} в тексте {text} = {second_sym_count}")

print("***** TASK 2 *****")

"""
Отобразить выходные данные: 
   IP-адрес: 4 числа, записанные через точку
   Пример: 10.11.12.33
"""
# number = int(input("Введите первое число: "))
# step = int(input("Введите шаг: "))
# summ = 0
# print("IP address: ", end=' ')
# for count in range(3):
#     print(number, end=".")
#     summ += number
#     number += step
# print(summ)

print("***** TASK 3 *****")
"""
Вывести из текста цифры и просуммировать их. Также отфильтровать текст и без номеров его вывести
"""

# text = input("Введите текст: ")
# summ = 0
# print("Отфильтрованный текст: ", end=' ')
# for symbol in text:
#     if symbol == '1' or symbol == '9':
#         summ += int(symbol)
#     else:
#         print( symbol, end='')
# print()
# print('sum: ', summ)


print("***** TASK 4 *****")
"""
Задача определить 2 одинаковые буквы которые идут подряд
"""
string = input("введите строку: ")
prev_sym = ''
equal_sym = False
for letter in string:
    if prev_sym == letter:
        equal_sym = True
        break
    else:
        prev_sym = letter
if equal_sym:
    print("Есть одинаковые буквы подряд")
else:
    print("Нет двух одинаковых букв подряд")
