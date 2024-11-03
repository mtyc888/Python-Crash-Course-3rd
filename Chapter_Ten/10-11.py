from pathlib import Path
import json

number = input("What's your fav number?")
path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)

print("I'll remember that number")