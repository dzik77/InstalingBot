import json
from Utilities import resoursce_path

class User:
    path = resoursce_path('user.json')
    login: str = ''
    password: str = ''
    def __init__(self):
        try:
            with open(self.path, 'r') as f:
                user = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            user = {}

        if user:
            self.login, self.password = list(user.items())[0]

    def dump_me(self, login: str, password: str):
        with open(self.path, 'w') as f:
            json.dump({login:password}, f)

    def clear_me(self):
        with open(self.path, 'w') as f:
            f.write('{}')