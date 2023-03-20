# The task

# 1. Create a function to check the password
# 2. The password must be at least 8 characters long
# 3. The password must have:
# - lower case letters
# - upper case letters
# - numbers special characters
# 4. Ask the user to enter the password in the terminal and verify it

import re

def password_check(password):
    password_regex = re.compile(r'^(?=(?:.*[a-z]){1})(?=(?:.*[A-Z]){1})(?=(?:.*\d){1})(?=(?:.*[!@#$%^&*()_\-+]){1})[a-zA-Z\d!@#$%^&*()_\-+]{8,32}$')
    # password_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_\-+])[a-zA-Z\d!@#$%^&*()_\-+]{8}$')
    password_check_pattern = re.compile(password_regex)
    validation_result = 'Valid' if password_check_pattern.fullmatch(password) else 'Not valid'
    return(password, validation_result)
    

while True:
    password = input("Enter password: ")
    result = password_check(password)
    if result[1] == 'Not valid':
        print("Password not valid! Please try again")
        continue
    else:
        print("Password is valid!")
        break
        
