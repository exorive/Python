Task

 1. Create any dictionary using keys with values of different types
 2. Convert the dictionary to json
 3. Output the resultant json to the terminal
 4. Output the type of the resulting value to the terminal

import json

my_dict = {
    "name": "Bob",
    "age": 25,
    "car": True,
    "salary": 5.5000
}

convert_to_json = json.dumps(my_dict, indent=2)

print(convert_to_json)
print(type(convert_to_json))
