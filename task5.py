# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Enter coordinates for point a: ')
x_a = int(input('x: '))
y_a = int(input('y: '))
print("Enter coordinates for a point a:")
x_b = int(input('x: '))
y_b = int(input('y: '))

from math import sqrt
print('The distance between a and b is: ', round(sqrt((x_a - x_b) ** 2 + (y_a - y_b) ** 2), 2))