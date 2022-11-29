# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)


number_n = int(input("Введите целое число: "))
factorials_list =[1]
i=1
while i<number_n:
    factorials_list.append(factorials_list[i-1]*(i+1))
    i+=1
print(factorials_list)