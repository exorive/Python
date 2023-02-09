# 1. Create a set with several int type elements
first_set = {112, 55, 100, 150, 105}

# 2. Add one more element to set
first_set.add(88)

# 3. Create another set, some elements must be repeated with the first set
second_set = {5, 9, 7, 55, 88}

# 4. Find the common elements in the two sets. Move them to the new set
new_set = first_set & second_set

# 5. Convert the set to a list and output to the terminal
my_list = list(new_set)
print(my_list)
print(type(my_list))
