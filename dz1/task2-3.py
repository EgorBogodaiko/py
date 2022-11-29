# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
from random import randint as rnd

n = int(input("Введите размер массива: "))
list_n =[]
i=0
for i in range (n):
    list_n.append(rnd(-30,30))
print('Изначальный массив:')
print(list_n)
i=0
while i<n:
    if list_n[i]<0:
        list_n.insert(i+1,0)
        i+=2
    else:
        i+=1
print('Обработанный массив:')
print(list_n)