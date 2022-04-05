print("TASK 2 гонка")

for row in range(20):
    for col in range(50):
        if row == 9: # если строка 2я, то рисуем пробелы
            print('-', end='')
        elif col == row +30:
            print('\\', end ='')
        elif col == -row+18:
            print('/', end ='')
        elif col == 24:
            print('|', end='')
        else:
            print(' ', end='')
    print()
