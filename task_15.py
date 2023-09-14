"""
Задача №15. Решение в группах
15. Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза
Input: 5 -> 5 1 6 5 9
Output: 1 9
"""

# lst = list(map(int, input("Введите числа: ").split(" ")))
# print(min(lst), max(lst))


# max = min = int(input("wm=>"))
# min_i = 0
# max_i = 0
# curr_i = 0

# for i in range(1, int(input("Введите кол-во арбузов"))):
#     wm =int(input("wm=>"))
#     if wm < min:
#         min = wm
#         min_i = i
#     if wm > max:
#         max = wm
#         max_i = i
# print(F"Минимальный вес = {min} и он на позиции = {min_i}")
# print(F"Максимальный вес = {max} и он на позиции = {max_i}")

# import random
# n = int(input("Введите количество арбузов: "))
# list = []

# Ввод веса каждого арбуза с клавиатуры
# i = 0
# while i < n:
#     temp = int(input(f"Введите вес {i+1} арбуза: "))
#     list.append(temp)
#     i +=1
# 

# # Ввод случайный чисел для примера весовых арбузов
# for _ in range(n):
#     list.append(random.randint(1, 12))
# print("Вес арбузов =", list)

# print("Самый легкий и самый тяжелый арбуз:", end=' ')
# print(min(list), "и", max(list), "кило, соответственно.")  
# print("Input: ", n, "-> ", " ".join(map(str, list)))
# print(f'Output: {min(list)} {max(list)}') 
# print()


m = int(input('Количество арбузов: '))
x = 1
melons = []

while m != 0:
    melons.append(int(input(f'Вес арбуза({x}): ')))
    m -= 1
    x += 1

light_m = hard_m = melons[0]
for i in range(len(melons)):
    if melons[i] > hard_m:
        hard_m = melons[i]
    elif melons[i] < light_m:
        light_m = melons[i]

print(f'Максимальный вес арбуза: {hard_m}')
print(f'Минимальный вес арбуза: {light_m}')