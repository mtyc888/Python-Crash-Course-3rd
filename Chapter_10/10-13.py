from pathlib import Path
import json

def get_stored_user_info(path):
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None
    
def get_new_user_info(path):
    username = input("What is your name")
    game = input("What is your fav game?")
    animal = input("What is your fav animal")

    user_dict = {
        'username':username,
        'game': game,
        'animal':animal
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['username']}!")
        print(f"Hope you've been playing some {user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']} recently?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you when you return, {user_dict['username']}!"
        print(msg)
        
greet_user()