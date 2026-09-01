import bcrypt
import json
from typing import Tuple
from datetime import datetime

# Handler Function
def hash_pwd(password:str, rounds=12) -> bytes:
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds))
    return pwd

def check_pwd(password:str, hash:bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hash)

def create_or_open(filename: str, default: dict = None) -> dict:
    data = default or {}
    try:
        with open(filename, "r", encoding='utf-8') as user_data:
            return json.load(user_data)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(filename, "w", encoding='utf-8') as user_data:
            json.dump(data, user_data, indent=4)

    return data

def save_json(filename: str, data: dict) -> bool:
    with open(filename, "w", encoding='utf-8') as user_data:
        json.dump(data, user_data, indent=4)
        return True

class UserAuth:
    def __init__(self):
        self.users = create_or_open('Users_data.json')
        self.login_attempts = create_or_open('login_attempts.json')
        self.max_attempts = 3
        self.lockout_minutes = 15

    def add_user(self, username:str, password:str) -> bool:
        if username in self.users:
            return False
        self.users[username] = {
            'pwd_hash': hash_pwd(password).decode('utf-8'), #using decode to convert bytes -> str
            'created_at': datetime.now().isoformat(), #using isoformat to convert datetime -> str
            'pwd_rounds': 12
        }
        save_json("Users_data.json", self.users)
        return True

    def login(self, username:str, password:str) -> Tuple[bool, str]:
        if self._is_locked(username):
            return False, 'Too many attempts, account is locked!'

        if username not in self.users:
            return False, 'User not found!'

        user = self.users[username]
        if not check_pwd(password, user['pwd_hash'].encode('utf-8')):
            self._track_attempts(username)
            save_json("login_attempts.json", self.login_attempts)
            return False, 'Incorrect password!'

        if username in self.login_attempts:
            self._upgrade_hash(username, password)
            del self.login_attempts[username]
            save_json("login_attempts.json", self.login_attempts)

        return True, 'Successfully logged in!'

    def _is_locked(self, username:str) -> bool:
        if username not in self.login_attempts:
            return False
        # {attempt:last_attempt}

        attempts, last_attempt = self.login_attempts[username]

        if attempts >= self.max_attempts:
            mins_passed = (datetime.now()-datetime.fromisoformat(last_attempt)).total_seconds() / 60
            if mins_passed < self.lockout_minutes:
                return True
            del self.login_attempts[username]

        save_json("login_attempts.json", self.login_attempts)
        return False

    def _track_attempts(self, username:str):
        now = datetime.now().isoformat()

        if username not in self.login_attempts:
            self.login_attempts[username] = (1, now)
            return

        attempts, _ = self.login_attempts[username]
        self.login_attempts[username] = (attempts + 1, now)
        save_json("login_attempts.json", self.login_attempts)

    def _upgrade_hash(self, username:str, password:str):
        user = self.users[username]
        min_rounds = 14
        if  user['pwd_rounds'] < min_rounds:
            user['pwd_hash'] = hash_pwd(password, min_rounds).decode('utf-8')
            user['pwd_rounds'] = min_rounds
        save_json("Users_data.json", self.users)

if __name__ == '__main__':
    auth = UserAuth()
    auth.add_user("admin", 'admin#04')
    auth.add_user("Darsh", "DarshKaPassword")

    state, msg = auth.login("Darsh", "EyMurkhApniChawiSudhaar")

    auth.login("admin", "admin#04")

