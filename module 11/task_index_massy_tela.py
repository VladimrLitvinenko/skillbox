"""
Задача "Индекс массы тела"

Возраст, рост (в метрах), вес (в кг)
ИМТ = вес/рост **2
ИМТ < 18.5 - недобор
    < 25 - норма
    < 30 - избыток
    >=30 - ожирение
"""

height = float(input('Ваш рост: '))
weight = float(input("Ваш вес: "))
body_mass_index = weight/height**2
print("Ваш индекс массы тела: ", body_mass_index)

if body_mass_index < 18.5:
    print("У вас недостаточная масса тела")
elif body_mass_index < 25:
    print("У вас нормальная масс тела")
elif body_mass_index < 30:
    print("У вас избыточная масса тела")
else:
    print("У вас ожирение")