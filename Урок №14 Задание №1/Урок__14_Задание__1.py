def print_list_recursive(my_list, index=0):
    # Проверяем, достигли ли конца списка
    if index < len(my_list):
        print(my_list[index])  # Выводим текущий элемент
        print_list_recursive(my_list, index + 1)  # Рекурсивный вызов для следующего элемента
    else:
        print("Конец списка")  # Сообщение о завершении

# Исходный список
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# Вызов функции
print_list_recursive(my_list)