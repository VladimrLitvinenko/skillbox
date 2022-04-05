print("TASK 1")
"""
Задача диагональ матрицы
N - размер матрицы
диагональ из единиц
Выше нули, ниже двойки
"""
size = 6
for row in range(size):
    for col in range(size):
        if row < col:
            print(0, end=' ')
        elif row > col:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print()



