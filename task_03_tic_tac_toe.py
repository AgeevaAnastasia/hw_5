# Создайте программу для игры в ""Крестики-нолики"".

print()
print \
    ('Вас приветствует консольная версия игры "Крестики-нолики"!'
    '\nЧтобы поставить Х или О, нужно выбрать координаты клетки, в которую его нужно поместить \nв формате "строка столбец"'
    '\nНапример, чтобы поместить Х в центр поля, нужно написать: 2 2, чтобы поместить в правый \nнижний квардрат, нужно написать: 3 3'
    '\nУдачи в игре!'
    )

from random import randint
print()
print()
pl_1 = input('Введите имя одного игрока: ')
pl_2 = input('Введите имя другого игрока: ')
print()
print('Провожу жеребьёвку...')
order = randint(1, 3)
input('Нажмите enter')
print()
if order == 2:
    player = pl_1
    pl_1 = pl_2
    pl_2 = player
print(f'Крестиками играет {pl_1}! Ноликами играет {pl_2}')
order = 1
print()
input(f'Нажмите enter')
print()


def print_field(used_x, used_o):
    for i in range(3):
        print('\n-------------')
        for j in range(4):
            if (i, j) in used_x:
                print('| X ', end = '')
            elif  (i, j) in used_o:
                print('| O ', end = '')
            else: print('|   ', end = '')
    print('\n-------------')
    print()


def if_win(used_x, used_o):
    if (0, 0) in used_x and (0, 1) in used_x and (0, 2) in used_x:
        return 1
    elif (1, 0) in used_x and (1, 1) in used_x and (1, 2) in used_x:
        return 1
    elif (2, 0) in used_x and (2, 1) in used_x and (2, 2) in used_x:
        return 1
    elif (0, 0) in used_x and (1, 0) in used_x and (2, 0) in used_x:
        return 1
    elif (0, 1) in used_x and (1, 1) in used_x and (2, 1) in used_x:
        return 1
    elif (0, 2) in used_x and (1, 2) in used_x and (2, 2) in used_x:
        return 1
    elif (0, 0) in used_x and (1, 1) in used_x and (2, 2) in used_x:
        return 1
    elif (2, 0) in used_x and (1, 1) in used_x and (0, 2) in used_x:
        return 1
    else: return 0


win = 0
cnt = 0
used_x = []
used_o = []
print_field(used_x, used_o)

while win == 0:
    if order == 1:
        (a, b) = (int(i) for i in input(f'Введите координаты, {pl_1}: ').split())
        temp = (a - 1, b - 1)
        if a < 1 or a > 3 or b < 1 or b > 3:
            print(f'{pl_1}, координаты каждой точки должны быть в пределах от 1 до 3')
            print()
            continue
        if temp in used_x:
            print('Данная клетка уже занята!')
            print()
            continue
        if temp in used_o:
            print('Данная клетка уже занята!')
            print()
            continue
        used_x.append(temp)
        order = 2
        print()
        
        print_field(used_x, used_o)
        win = if_win(used_x, used_o)
        cnt += 1
        
    elif order == 2 and cnt < 9:
        (a, b) = (int(i) for i in input(f'Введите координаты, {pl_2}: ').split())
        temp = (a - 1, b - 1)
        if a < 1 or a > 3 or b < 1 or b > 3:
            print(f'{pl_2}, координаты каждой точки должны быть в пределах от 1 до 3')
            print()
            continue
        if temp in used_o:
            print('Данная клетка уже занята!')
            print()
            continue
        if temp in used_o:
            print('Данная клетка уже занята!')
            print()
            continue
        used_o.append(temp)
        order = 1
        print()
        print_field(used_x, used_o)
        win = if_win(used_x, used_o)
        cnt += 1
    if cnt == 9:
        win = 2 


if order == 2 and win == 1:
    print(f'Победитель {pl_1}!')
elif order == 1 and win == 1:
    print(f'Победитель {pl_2}!')
elif win != 1: 
    print('У нас ничья!')
