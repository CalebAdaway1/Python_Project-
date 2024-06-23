import json
from models import Task

class FileAccess:
    @staticmethod
    def load_tasks(file_path):
        try:
            with open(file_path, 'r') as file:
                tasks = json.load(file)
                return [Task(**task) for task in tasks]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_tasks(file_path, tasks):
        with open(file_path, 'w') as file:
            json.dump([task.__dict__ for task in tasks], file)