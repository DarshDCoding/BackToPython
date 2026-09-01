import bcrypt
from typing import Tuple
from datetime import datetime

# Handler Function
def hash_pwd(password:str, rounds=12) -> bytes:
    pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds))
    return pwd

def check_pwd(password:str, hash:bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hash)

class UserAuth:
    def __init__(self):
        self.users ={}
        self.login_attempts = {}
        self.max_attempts = 3
        self.lockout_minutes = 15

    def add_user(self, username:str, password:str) -> bool:
        if username in self.users:
            return False
        self.users[username] = {
            'pwd_hash': hash_pwd(password),
            'created_at': datetime.now(),
            'pwd_rounds': 12
        }
        return True

    def login(self, username:str, password:str) -> Tuple[bool, str]:
        if self._is_locked(username):
            return False, 'Too many attempts, account is locked!'

        if username not in self.users:
            return False, 'User not found!'

        user = self.users[username]
        if not check_pwd(password, user['pwd_hash']):
            self._track_attempts(username)
            return False, 'Incorrect password!'

        if username in self.login_attempts:
            self._upgrade_hash(username, password)
            del self.login_attempts[username]

        return True, 'Successfully logged in!'

    def _is_locked(self, username:str) -> bool:
        if username not in self.login_attempts:
            return False
        # {attempt:last_attempt}

        attempts, last_attempt = self.login_attempts[username]

        if attempts >= self.max_attempts:
            mins_passed = (datetime.now()-last_attempt).total_seconds() / 60
            if mins_passed < self.lockout_minutes:
                return True
            del self.login_attempts[username]
        return False

    def _track_attempts(self, username:str):
        now = datetime.now()

        if username not in self.login_attempts:
            self.login_attempts[username] = (1, now)
            return

        attempts, _ = self.login_attempts[username]
        self.login_attempts[username] = (attempts + 1, now)

    def _upgrade_hash(self, username:str, password:str):
        user = self.users[username]
        min_rounds = 14
        if  user['pwd_rounds'] < min_rounds:
            user['pwd_hash'] = hash_pwd(password, min_rounds)
            user['pwd_rounds'] = min_rounds

if __name__ == '__main__':
    auth = UserAuth()

    user = "DarshD.Coding"
    password = "MaiPapaHuIsDuniyaKaPapa"

    if auth.add_user(user, password):
        print("Account Created!")

    success, msg = auth.login(user, password)
    print("Good Login:", msg)

    for i in range(4):
        success, msg = auth.login("DarshD.Coding", "mePapaHu")
        print(f"Bad Login: {i+1}: {msg}")

    success, msg = auth.login("DarshD.Coding", "MaiPapaHuIsDuniyaKaPapa")
    print(msg)