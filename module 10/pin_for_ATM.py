while True:
    for attempt in range(1,4):
        pincode = int(input("Введите пин-код: "))
        if pincode == 1234:
            print("Пинкод верный. Возьмите деньги")
            break
        print(f"Неверный пинкод. Осталось {attempt} попыток")
    else:
        print("Карта заблокана")
    print("Следующий клиент. Добро пожаловать!")
