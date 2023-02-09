# 1. Create a function 'image_info' with one parameter of type dict
# 2. The function expects a dictionary with at least two keys:
#    image_id
#    image_title
# 3. The function should return a string of this form:
#    "Image 'my cat' has id 5136"
# 4. If at least one of these keys is not in the dictionary, the function should generate error TypeError
# 5. Call the function and correctly handle the error if it occurs


def image_info(my_dict):
    try:
        if 'image_id' not in my_dict or 'image_title' not in my_dict:
            raise TypeError("The dictionary must contain two required keys 'image_id' and 'image_title'")
        result = f"Image {my_dict['image_title']} has id {my_dict['image_id']}"
        return result
    except TypeError as e:
        print(e)


new_dict = {'image_id': 6549, 'image_title': 'my cat'}
first_dict = {'color_id': 49, 'image_title': 'my cat'}
second_dict = {'image_id': 6549, 'age': 1}

result_a = image_info(new_dict)
print(result_a)

print('===========')

result_b = image_info(first_dict)
print(result_b)

print('===========')

result_c = image_info(second_dict)
print(result_c)

print('Continue')
