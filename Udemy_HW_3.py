# 1. Create an empty dictionary
employees = {}

# 2. Request data from the user
# There should be a total of 6 data entry requests
while len(employees) < 3:
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    employees[name] = salary

# 3. Add two more keys
employees['Mary'] = 100
employees['Nonipa'] = 100

# 4. Delete one key
del employees['Bob']

print(employees)