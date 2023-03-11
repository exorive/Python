# Задача

# 1. Создайте папку files в текущей папке
# 2. Добавьте два файла first.txt и second.txt в эту папку и запишите в них
# по 2-3 строки текста
# 3. Прочитайте все строки первого файла
# 4. Прочитайте строки второго файла одна за другой
# 5. Удалите оба файла
# 6. Удалите папку files

from pathlib import Path

files = Path('files')

if not files.exists():
    files.mkdir()

with open (files / 'first.txt', 'w') as first_file:
    first_file.write("First string\n")
    first_file.write("Second string\n")
    first_file.write("Third string\n")

with open (files / 'second.txt', 'w') as second_file:
    second_file.write("First string in second file\n")
    second_file.write("Second string in second file\n")
    second_file.write("Third string in second file\n")

with open(files / 'first.txt', 'r') as first_file:
    print(first_file.read())

with open(files / 'second.txt', 'r') as second_file:
    print(second_file.readline())
    print(second_file.readline())
    print(second_file.readline())

# option 1
# with open(files / 'second.txt', 'r') as second_file:
#    for line in second_file:
#        print(line.strip())

#option 2

#while True:
#    line = second_file.readline()
#    if not line:
#        break
#    print(line.strip())

first_file_txt = Path(files / 'first.txt')

if first_file_txt.exists():
    first_file_txt.unlink()

second_file_txt = Path(files / 'second.txt')

if second_file_txt.exists():
    second_file_txt.unlink()

if files.exists():
    files.rmdir()

