# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.
def defenition(x, y, z):
    if (not (x or y or z)) == ((not x) and (not y) and (not z)):
        return True
    else:
        return False

pred_x = bool
pred_y = bool
pred_z = bool
print('Утверждение к проверке:  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print('X   Y   Z - result')
string_input = "1000"
for i in range (1,9):
    print(string_input[1], ' ', string_input[2], ' ', string_input[3], '-', defenition(bool(string_input[1]), bool(string_input[2]), bool(string_input[3])))
    j= str(bin(i))
    j=int(j[2:5])
    string_input=int(1000+j)
    string_input=str(string_input)
