# Task 1.
#
# 1. Create a function dict_to_list that converts a dictionary into a tuple list
# 2. The function should take the dictionary and return a list of tuples each tuple should contain pairs (key, value) from the dictionary
# 3. if the value of the key is an integer, it should be multiplied by 2 before being added to the tuple


def dict_to_list(my_dict):
    my_list = []
    for item in my_dict.items():
        key, value = item
        if type(value) is int:
            value *= 2
        my_list.append((key, value))
    return my_list


a = {
    'a': 5,
    'b': 10,
}

print(dict_to_list(a))
# [('a', 10), ('b', 20)]


# Task 2.
#
# 1. Create a filter_list function that will filter the list
# 2. The function must have two parameters - list and value type
# 3. The function should return a new list with only values of the type that was passed as second argument in the function call
# 4. The function can be called like this filter_list([35, True, 'abc', 10], int) and get [35, 10]

def filter_list(list_data, list_type):
    new_list = []
    for i in list_data:
        if type(i) == list_type:
            new_list.append(i)
    return new_list


test_list = [True, 100, 'Bob', {}, [], 5, 'salary', 8000]

print(filter_list(test_list, str))
print(filter_list(test_list, int))
print(filter_list(test_list, bool))
# ['Bob', 'salary']
# [100, 5, 8000]
# [True]



