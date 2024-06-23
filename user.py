import json

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email
        }

class UserManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                users = json.load(file)
                return [User(**user) for user in users]
        except FileNotFoundError:
            return []

    def save_users(self):
        with open(self.file_path, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def add_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users.append(user)
        self.save_users()

    def get_users(self):
        return self.users