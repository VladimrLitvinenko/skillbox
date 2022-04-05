print("TASK 1")
"""
N размер квадратной матрицы
В строке - числа от 1 до N
В каждой второй номер строки N раз
"""
size = 4 # int(input("Введите размер таблицы: "))
for row in range(1, size+1):
    for col in range(1, size +1):
        if row % 2 == 0:
            print(row, end=" ")
        else:
            print(col, end=" ")
    print()

print("ЗАДАЧА НА КООРДИНАТНЫЕ ОСИ")
for row in range(20):
    for col in range(50):
        if row == 9: # если строка 2я, то рисуем пробелы
            print('-', end='')
        elif col == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print()