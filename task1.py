# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input('Enter a weekday number, please: '))
if 0 < num < 6:
    print(num, 'is not a weekend.')
elif 5 < num < 8:
    print(num, 'is a weekend.')
else:
    print(num, 'is not a weekday number!')