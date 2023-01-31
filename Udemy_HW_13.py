# 1. Create a list of three dictionaries
# 2. Use the unpack list operator to create three variables, each containing one of the dictionaries
# 3. Create a function that takes two arguments
# 4. When the function is called the dictionary must be unpacked
# 5. Call the function three times


my_list = [
    {'name': 'Bob', 'age': 25},
    {'name': 'Alice', 'age': 32},
    {'name': 'John', 'age': 40}
]

a_info, b_info, c_info = my_list


def my_function(name, age):
    print(f"Name: {name}, Age: {age}")


my_function(**a_info)
my_function(**b_info)
my_function(**c_info)








