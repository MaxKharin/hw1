# Напишите программу, которая принимает на вход
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter x: '))
y = int(input('Enter y: '))

if x > 0 and y > 0:
    print('The dot is in the first quarter.')
elif x < 0 and y > 0:
    print('The dot is in the second quarter.')
elif x < 0 and y < 0:
    print('The dot is in the third quarter.')
elif x > 0 and y < 0:
    print('The dot is in the fourth quarter.')
else:
    print('Please, enter integer numbers, that are not equal to 0.')