# 1. Create the merge_lists_to_dict function
# 2. The function must have two parameters 
# 3. The function must merge two lists (use the zip function)
# 4. Convert the zip object to a dictionary and return it from the function (using return)
# 5. Call the function by passing the two lists as arguments
# 6. Print the result of the function call to the terminal


def merge_lists_to_dict(a, b):
    combined_list = zip(a, b)
    combined_dict = dict(combined_list)
    return combined_dict


first_list = ['one', 'two', 'tree', 'four']
second_list = [1, 2, 3, 4]

res = merge_lists_to_dict(first_list, second_list)
print(res)

# {'one': 1, 'two': 2, 'tree': 3, 'four': 4}