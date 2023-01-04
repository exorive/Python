# 1. Create two lists
summer_months = ['june', 'July', 'August']
autumn_months = ['September', 'October', 'November']

# 2. Combine two lists using the + operator
combined_months = summer_months + autumn_months

# 3. Determine which list megic method is called when using the + operator
print(dir(combined_months))

# 4. Perform list merge using this magic method
combined_months = summer_months.__add__(autumn_months)

# 5. Output the result to the terminal
print(combined_months)