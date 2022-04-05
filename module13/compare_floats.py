a = 1.1
b = 2.2
c = a + b
d = 3.3

if abs(c-d) < 1e-1:
    print('Равна', abs(c-d))
else:
    print("Не равна")