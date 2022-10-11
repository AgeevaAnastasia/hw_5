# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не 
# хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

def get_data_from_file(nums):
    data = open(nums, 'r')
    l = data.read() + ' '
    l = list(map(int, l.split()))
    data.close()
    return l


def find_number(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1


fnums = 'task_35.txt'
nums_list = get_data_from_file(fnums)

print(nums_list)
print(f'число, которого не хватает в файле task_35 для выполнения условия A[i] - 1 = A[i-1] - это {find_number(nums_list)}')

nums = get_data_from_file(fnums)
