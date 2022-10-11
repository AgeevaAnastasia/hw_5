# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?


from random import randint
print()
print('Привет! Это игра "Возьми конфеты". \nНа столе лежит 2021 конфета. \nИграют 2 игрока друг против друга. Первый ход определяется жеребьёвкой. \nЗа один ход можно взять от 1 до 28 конфет, пропустить ход нельзя. \nПобеждает тот, кто заберет последнюю конфету - ему достанутся все конфеты! \nУдачи!')
print()
pl_1 = input('Введите имя одного игрока: ')
pl_2 = input('Введите имя другого игрока: ')
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
        candies_taken = int(input(f'Сейчас на столе конфет: {candies_all}. \n{pl_2}, введите число конфет от 1 до 28, которые вы хотите взять: '))
        if candies_taken < 1 or candies_taken > 28:
            print(f'{pl_2}, вы можете взять от 1 до 28 конфет, не больше и не меньше!')
            print()
            continue
        candies_all -= candies_taken
        order = 1
        print()
        if candies_all > 0:
            print(f'Теперь ходит {pl_1}!')
            print()

if order == 1:
    print(f'Победитель игры - {pl_2}! Забирайте все конфеты, приятного аппетита!')
else:
    print(f'Победитель игры - {pl_1}! Забирайте все конфеты, приятного аппетита!')
    
print('До встречи в новой игре!')
print()

    
