print(""
      "TASK 1"
      "")
# Задача "Счастливый билет"
winner = 0
for ticket in 5, 14134, 5134, 134, 355, 10:
    if ticket % 5 == 0:
        print(ticket)
        winner += 1
print(f"кол-во победителей с счастливым билетом который делится на 5 = {winner}")

print(""
      "TASK 2 test"
      "")
# Задача "во сколько проснулись"
# Засыпаем в 23 если сьели больше 2000 калоррий

wake_up = int(input("Во сколько проснулись: "))
awake_hours = 0
calories_sum = 0
for hour in range(wake_up, 23):
    print("Сейчас ", hour, "часов")
    calories = int(input("Сколько съел за час? "))
    calories_sum += calories
    if calories_sum > 2000:
        print('Хорошо поел, можно поспать')
        break
    awake_hours +=1
print("Съедено калорий за день: ", calories_sum)
print("Часов не спал: ", awake_hours)
