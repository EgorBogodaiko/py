# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_week=int( input('Введите номер дня недели: '))
if ((day_week > 7) or (day_week < 1)): print('Это не день недели, вводите чиcло из диапазона от 1 до 7')
elif (day_week > 5): print('Да, выходной')
else:print('Нет, будний')
