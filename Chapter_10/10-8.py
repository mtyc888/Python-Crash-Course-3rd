from pathlib import Path

filenames = ['cats.txt','dogs.txt']

for filename in filenames:
    print(f"\n Reading file: {filename}")

    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("No such file")
    else:
        print(contents)