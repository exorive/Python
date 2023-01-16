# 1. Create a function update_car_info in which all named arguments are combined into the car dictionary.
# 2. Add to the dictionary a new key is_available with value True
# 3. Return the modified dictionary from the function.
# 4. Call the function with named arguments brand and price, their values can be any.
# 5. Print the result of the function to the terminal.

def update_car_info(**car):
    print(type(car))
    car['is_available'] = True
    return car

my_dict = update_car_info(brand='Audi ', price=5000)
print(my_dict)

# <class 'dict'>
# {'brand': 'Audi ', 'price': 5000, 'is_available': True}