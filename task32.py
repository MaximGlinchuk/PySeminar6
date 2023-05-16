import random

list1 = [random.randint(1,20) for _ in range(10)]
diap_min = int(input('Введите минимальный порог: '))
diap_max = int(input('Введите максимальный порог: '))
print(list1)
for i in range(len(list1)):
    if list1[i] >= diap_min and list1[i] <= diap_max:
        print(i, end=' ')