def calculate_tax(price, tax):
    total = price + (price + tax / 100)
    print(total)
    return total


my_price = float(input("Введите цену: "))
my_tax = int(input('Введите налог'))

total_price = calculate_tax(my_price, my_tax)
