my_list = [42, 69, 322, 13, 0, 99, 9, 8, 7, 5]
index = -1
len_list = len(my_list)
while index < len_list-1:
    index = index +1
    if my_list [index] >0:
        print(my_list[index])
        continue
    elif my_list[index]==0:
        continue
    else:
        print('Работа цикла прекращена: отрицательное значение')
        break
if index ==len(my_list)-1:
    print('Конец списка')