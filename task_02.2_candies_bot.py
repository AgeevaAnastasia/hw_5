# Создайте программу для игры с конфетами человек против компьютера.
# Подумайте как наделить бота ""интеллектом""

from random import randint
print()
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \nПривет! Это игра "Возьми конфеты". \nНа столе лежит 2021 конфета. \nИграют 2 игрока друг против друга. Первый ход определяется жеребьёвкой. \nЗа один ход можно взять от 1 до 28 конфет, пропустить ход нельзя. \nПобеждает тот, кто заберет последнюю конфету - ему достанутся все конфеты! \nУдачи! \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print()
pl_1 = input('Введите имя игрока: ')
name_dict = {1: 'Электроник', 2: 'Хитрый Лис', 3: 'Настоящий мальчик', 4: 'Зорро', 5: 'Мистер Икс'}
random_name = randint(1, 6)
pl_2 = name_dict.get(random_name)
print(f'Сегодня против вас играет {pl_2}')
print()
print('Провожу жеребьёвку...')
order = randint(1, 3)
input('Нажмите enter')
print()
candies_all = 2021
if order == 1:
    print(f'Сначала ходит {pl_1}!')
    print()
else: print(f'Сначала ходит {pl_2}!')
input(f'Нажмите enter')
print()

while candies_all > 0:
    if order == 1:
        candies_taken = int(input(f'Сейчас на столе конфет: {candies_all}. \n{pl_1}, введите число конфет от 1 до 28, которые вы хотите взять: '))
        if candies_taken < 1 or candies_taken > 28:
            print(f'{pl_1}, вы можете взять от 1 до 28 конфет, не больше и не меньше!')
            print()
            continue
        candies_all -= candies_taken
        order = 2
        print()
        if candies_all > 0:
            print(f'Теперь ходит {pl_2}!')
            print()
    elif order == 2:
        if random_name == 1 or random_name == 2:
            candies_taken = candies_all % 29            
        elif random_name == 3 or random_name == 4 or random_name == 5:
            candies_taken = randint(1, 29)
        print(f'{pl_2} берет конфет со стола: {candies_taken}')    
        candies_all -= candies_taken
        order = 1
        print()
        if candies_all > 0:
            print(f'Теперь ходит {pl_1}!')
            print()

if order == 1:
    print(f'Победитель игры - {pl_2}! Увы, {pl_1}, удача сегодня не на вашей стороне...')
else:
    print(f'Вы победили, {pl_1}! Забирайте все конфеты, приятного аппетита!')
    
print('До встречи в новой игре!')
print()
