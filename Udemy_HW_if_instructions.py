# 1. Create a route_info function to pass the dictionary to
# 2. If the dictionary has a distance key and its value is an integer, return the string "Distance to your destination is <distance>".
# 3. Otherwise, if the dictionary has speed and time keys, return the string "Distance to your destination is <speed * time>".
# 4 Otherwise return the string "No distance info is available".
# 5. Call the function several times with different arguments


def route_info(route):
    if ('distance' in route) and (type(route['distance']) == int):
        return f"Distance to your destination is {route['distance']}"

    if ('speed' in route) and ('time' in route):
        return f"Distance to your destination is {route['speed'] * route['time']}"

    return "No distance info is available"


my_dict_a = {
    'distance': 200,
    'speed': 60,
    'time': 2,
}

my_dict_b = {
    'speed': 60,
    'time': 2,
}

my_dict_c = {
    'transport': 'car',
    'color': 'red',
    'time': 2,
}


print(route_info(my_dict_a))
print(route_info(my_dict_b))
print(route_info(my_dict_c))

