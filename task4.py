# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quart_num = int(input('Please, enter a quarter number: '))
if 0 < quart_num < 5:
    if quart_num == 1:
        print('Possible point coordinates are x > 0 and y > 0')
    elif quart_num == 2:
        print('Possible point coordinates are x < 0 and y > 0')
    elif quart_num == 3:
        print('Possible point coordinates are x < 0 and y < 0')
    elif quart_num == 4:
        print('Possible point coordinates are x > 0 and y < 0')
else:
    print(quart_num, 'is not a quarter number! Please, enter an integer number from 1 to 4.')