# Дан список чисел. Создайте список, в который попадают числа, описываемые
# возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

numbers = [1, 5, 2, 3, 4, 6, 1, 7]

def increased1(nums):
    l_1 = [nums[0]]
    for i in nums:
        if i > max(l_1):
            l_1.append(i)
    return l_1


def increased2(nums):
    l_1 = []
    for i in range(len(nums)):
        if i in nums:
            l_1.append(i)
            nums[i] = -1
    return l_1

print(f'{numbers} => ')
print(increased1(numbers))
print(increased2(numbers))

