first_element = int(input('Введите первый элемент: '))
step_element = int(input('Введите разность между элементами: '))
size_element = int(input('Введите размер списка: '))

list = [(first_element + i * step_element) for i in range(size_element)]
print(list)