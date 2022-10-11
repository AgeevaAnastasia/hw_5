# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

print()
print()
print \
    ('Нуклеотидные последовательности ДНК записываются буквами латинского алфавита, где \nA = аденин, \nC = цитозин, \nG = гуанин и \nT = тимин.' 
    '\nДля кодирования dna применяется метод RLE-кодирования. \nКодирование осуществляется следующим образом:'
    '\ndna = "AAAABBCAA" преобразуется в "A4B2C1A2", \nто есть группы одинаковых символов исходной строки заменяются на этот символ \nи количество его повторений в этой позиции строки.'
    )

print()
print()
choice = input('Если вы желаете провести кодирование dna выберите на клавиатуре "C", если раскодирование - выберите "D": ')
print()

if choice == "C" or choice == "c":
    dna = input('Введите последовательность нуклеотидов для кодирования: ')
    dna = dna.upper()
    l = len(dna) - 1
    if len(dna) == 1:
        print(f'{dna[0]}1')
    cnt = 1
    i = 0
    while i < l:
        if dna[i] == dna[i + 1]:
            cnt += 1
            i += 1
        elif dna[i] != dna[i + 1]: 
            print(f'{dna[i]}{cnt}', end='')
            i += 1
            cnt = 1
        if i == l:
            print(f'{dna[i]}{cnt}')
 
elif choice == "D" or choice == "d":
    dna_code = input('Введите закодированную нуклеотидную последовательность: ')
    dna_code = dna_code.lower()
    dna_temp = []
    temp = ''
    for i in range(len(dna_code)):
        if not dna_code[i].isdigit():
            if temp != '':
                dna_temp.append(temp)
                temp = ''
            dna_temp.append(dna_code[i])
        if dna_code[i].isdigit():
            temp += dna_code[i]
    if temp != '':
        dna_temp.append(temp)
        temp = ''
    
    i = 0
    dna = ''
    while i <= len(dna_temp) - 1:
        temp = dna_temp[i] * int(dna_temp[i+1])
        dna += temp
        i += 2
    dna = dna.upper()
    print(dna)
