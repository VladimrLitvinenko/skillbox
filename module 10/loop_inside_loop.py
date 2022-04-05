print("TASK 1 создадим таблицу умножения")
for a in range(1, 10):
    for b in range(1, 10):
        print(a, " * ", b, "= ", a * b)
    print()

print("TASK 2 создадим таблицу из цифр")
for row in range(6):
    for col in range(6):
        print(row + col, end=" ")
    print()

print("TASK 3 еще одна таблицы")
"""count = 1
for row_1 in range(1,10):
    for col_1 in range(1, 10):
        print(col_1, end="\t")
    print()"""

print("TASK 4 count. Задача 2. Таблица суммы")
input_i = 6
for row in range(input_i + 1):
    for col in range(input_i + 1):
        print(row + col, end='\t')
    print()

print("TASK 4 count. Задача 3. Анализ данных")
for line in range(10):
    for column in range(0, 10):
        print(line - column, end="\t")
    print()
