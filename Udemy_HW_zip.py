# 1.Create a list with product names 
products = ['apple', 'banana', 'lime']

# 2. Create a list with prices
prices = [25, 70, 55]

# 3. Combine lists
combined_zip = zip(products, prices)

# 4. Convert to a list
combined_zip_list = list(combined_zip)

# 5. Output the result to the terminal
print(combined_zip_list)
# [('apple', 25), ('banana', 70), ('lime', 55)]

