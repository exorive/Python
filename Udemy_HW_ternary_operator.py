my_img = ('1920', '1080')

info = f"{my_img[0]}x{my_img[1]}" if len(
    my_img) == 2 else "Incorrect image formatting"

print(info)


my_img = ('1920', '1080')

if len(my_img) == 2:
    info = f"{my_img[0]}x{my_img[1]}"
else:
    info = "Incorrect image formatting"


print(info)


my_str = "Its a very very very long string"

if len(my_str) >= 12:
    len_message = "The string is long"
else:
    len_message = "The string is short"


print(len_message)

