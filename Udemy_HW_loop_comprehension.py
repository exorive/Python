# Task 1.
# 1. Create a dictionary with several keys whose values must be of type str
# 2. Create a new dictionary based on the existing one, where all the keys' values should be in uppercase
# 3. Output the resulting dictionary to the terminal

my_dict = {
    'name': 'bob',
    'company': 'letyshops',
    'position': 'qa'
}

new_dict = {k: v.upper() for k, v in my_dict.items()}

print(new_dict)


# Task 2.
# 1. Create a list with elements of type str
# From this list, create a new list with only strings longer than 5
# 3. Output the resulting list to the terminal

my_list = ['apple', 'banana', 'tangerine', 'plum', 'laim', 'lemon']

new_list = [item for item in my_list if len(item) > 5]

print(new_list)


