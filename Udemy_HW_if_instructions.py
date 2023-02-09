# 1. Create a route_info function to pass the dictionary to
# 2. If the dictionary has a distance key and its value is an integer, return the string "Distance to your destination is <distance>".
# 3. Otherwise, if the dictionary has speed and time keys, return the string "Distance to your destination is <speed * time>".
# 4 Otherwise return the string "No distance info is available".
# 5. Call the function several times with different arguments


def route_info(a):
    if a.get('distance') and type(a['distance']) is int:
        return f"Distance to your destination is {a['distance']}"

    if a.get('speed') and a.get('time'):
        b = a['speed'] * a['time']
        return f"Distance to your destination is {b}"

    if not a.get('distance') or type(a['distance']) is not int:
        return "No distance info is available or distance is not integer"


my_dict_f = {
    'distance': 200,
    'speed': 60,
    'time': 2,
}

my_dict_d = {
    'speed': 60,
    'time': 2,
}

my_dict_dd = {
    'transport': 'car',
    'color': 'red',
    'time': 2,
}


print(route_info(my_dict_f))
print(route_info(my_dict_d))
print(route_info(my_dict_dd))

