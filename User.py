import json
from Utilities import resoursce_path

class User:
    path = resoursce_path('user.json')
    login: str = ''
    password: str = ''
    parentAccount: bool = False
    def __init__(self):
        try:
            with open(self.path, 'r') as f:
                user = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            user = []

        if user:
            self.login, self.password, self.parentAccount = user

    def dump_me(self, login: str, password: str, parentAccount: bool):
        with open(self.path, 'w') as f:
            json.dump([login,password,parentAccount], f)

    def clear_me(self, parentAccount: bool):
        with open(self.path, 'w') as f:
            json.dump(["","",parentAccount],f)