import secrets
import string

all_chars = string.ascii_letters + string.digits + string.punctuation
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

print(''.join(secrets.choice(all_chars) for i in range(20)))
# #\Ek6k~D5q:\CKV]+I#;
# simple password generator
