# 1. Create two variables and assign them the same sequences of type set. Do not copy one variable into the other.
# 2. Output the result of the comparison of the two created objects to the terminal and explain the result.
# 3. Compare the two objects using the is operator, explain the result.
# 4. Check if there are certain items in the set using the in operator.

first_set = {'apple', 'banana', 'lime'}
second_set = {'apple', 'lime', 'banana'}

print(first_set == second_set) # True

print(first_set is second_set) # False

print('apple' in first_set) # True