# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

text = input('введите текст: ').split()

for item in text:
    if "абв" in item:
        text.remove(item)

print(text) 