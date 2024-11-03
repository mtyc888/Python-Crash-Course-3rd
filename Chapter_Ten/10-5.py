from pathlib import Path

path = Path("guest_book.txt")
name_list = []

while True:
    name = input("What is your name?")
    if name == 'stop':
        break
    name_list.append(name)
    
file_string = ''

for name in name_list:
    file_string = file_string +  f"{name}\n"
path.write_text(file_string)