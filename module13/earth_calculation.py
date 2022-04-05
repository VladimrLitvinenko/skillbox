v_first_planet = 1.43128e15  # km^3
v_second_planet = 6.254e13  # km^3
p_earth = 5.515e12  # кг/km^3

m_first_planet = float(input('Масса первой планеты: '))
m_second_planet = float(input('Масса второй планеты: '))

# Чтоб найти плотность, то нужно массу поделить на объем
p_first_planet = m_first_planet / v_first_planet
p_second_planet = m_second_planet / v_second_planet
print('Плотность первой планеты: ', p_first_planet)
print('Плотность второй планеты: ', p_second_planet)

if abs(p_earth - p_first_planet) < abs(p_earth - p_second_planet):
    print("Плотность первой планеты ближе к плотности Земли")
else:
    print("Плотность второй планеты ближе к плотности Земли")
