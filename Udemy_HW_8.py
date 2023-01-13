def merge_lists_to_dict(a, b):
    combined_list = zip(a, b)
    combined_dict = dict(combined_list)
    return combined_dict


first_list = ['one', 'two', 'tree', 'four']
second_list = [1, 2, 3, 4]

res = merge_lists_to_dict(first_list, second_list)
print(res)

# {'one': 1, 'two': 2, 'tree': 3, 'four': 4}


# 1. Создайте функцию merge_lists_to_dict
# 2. Функция должна иметь два параметра 
# 3. Функция должна объединять два списка (используйте функцию zip)
# 4. Конвертируйте объект zip в словарь и верните его из функции (используя return)
# 5. Вызовите функцию передав ей два списка в качестве аргументов
# 6. Выведите результат вызова функции в терминал