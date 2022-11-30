# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

realnumber = input("Введите вещественное число: ")
sumdigits = 0
if is_float(realnumber) == False:
    print('Введено не вещественное число')
else:
    for num in realnumber:
        if num.isdigit():
            sumdigits += int(num)
    print('Сумма цифр в числе: ', sumdigits)