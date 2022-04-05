print("Задача 1. Врата")

for row in range(10):
    for col in range(30):
        if row == 0:
            print('-', end= '')
        elif col < 1:
            print('|', end=' ')
        elif col == 28:
            print('|', end='')
        else:
            print(' ', end='')
    print('')
print("Задача 2. Дорога")
for row2 in range(20):
    for col2 in range(50):
        if row2 == 9:
            print('-', end='')
        elif col2 == row2+27:
            print('\\', end='')
        elif col2 == -row2+20:
            print('/', end='')
        elif col2 == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print('')

print("Задача 3. Диагональная матрица")

for row3 in range(5):
    for col3 in range(5):
        if -row3+4 == col3:
            print(1, end='')
        elif -row3+4 < col3:
            print(2, end='')
        else:
            print('0', end='')
    print('')
print("""
test
""")

for row4 in range(10):
    for col4 in range(5):
        print(f'col={col4}+row={row4}',end=' ')
    print('')