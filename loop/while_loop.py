# TASK 1
weather = 5  # int(input("How much of degree? "))
meters = 0
while weather > 15:
    meters += 20  # run a little bit ahead
    weather -= 2  # became cold
    if weather <= 15:
        break
    meters += 10  # jogged a little bit
print("Meters past: ", meters)

# TASK 2
number = int(input("Enter number: "))
summ = 0
while number != 0:
    last_num = number % 10
    print("last number = ", last_num)
    if last_num == 5:
        print("Break is detected")
        break
    summ += last_num
    number //= 10
print("Sum = ", summ)

