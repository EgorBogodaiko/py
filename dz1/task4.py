# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

quarter = int(input("Введите четверть: "))

if quarter == 2:
    print('В четверти 2: x∈(-∞, 0) u y∈(0,∞)')
elif quarter == 3:
    print('В четверти 3: x∈(-∞, 0) u y∈(-∞, 0)')
elif quarter == 1:
    print('В четверти 1: x∈(0, ∞) u y∈(0,∞)')
elif quarter == 4:
    print('В четверти 4: x∈(0, ∞) u y∈(-∞, 0)')
elif quarter<1 or quarter>4:
    print('Четверти не существует')