# # 4 - По кругу стоят n человек.
# Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.
# Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

players_qty = int(input("Количество человек в круге: "))
counter_def = int(input("Считалка считает до: ")) % players_qty
winner = 0
winners_coins = 0
players_list = []
cash_list = []
i = 1
counter_var = 0
j=0
for i in range(players_qty):
    players_list.append(i)
    cash_list.append(0)
print('начало ')
print(players_list)
print(cash_list)

while players_qty > 1:
    if counter_def>players_qty:
        counter_def = (counter_def % players_qty)
    print('считалка ',counter_def)
    counter_var=0
    while counter_var < len(players_list):
        if counter_var < counter_def:
            cash_list[counter_var] += 1
        elif counter_var >= counter_def:
            cash_list[counter_var] += 2
        if counter_var == counter_def-1:
            if counter_def==players_qty:
                cash_list[0]+=cash_list[counter_var]
            else: 
                cash_list[counter_var+1]+=cash_list[counter_var]
        counter_var+=1
    if (counter_def==players_qty):
        players_list = players_list[:counter_def-1:1]
        cash_list = cash_list[:counter_def-1:1]
    else:
        players_list = players_list[counter_def::1]+players_list[:counter_def-1:1]
        cash_list = cash_list[counter_def::1]+cash_list[:counter_def-1:1]
    players_qty=players_qty-1

    j+=1
    print('после круга ',j)
    print(players_list)
    print(cash_list)
print(players_list, cash_list)
