import json
import os

class StorageManager:
    File_name = 'library_data.json'

    @staticmethod
    def save_data(data):
        with open(StorageManager.File_name, 'w') as f:
            json.dump(data, f, indent=4)

    
    @staticmethod
    def load_data():
        if not os.path.exists(StorageManager.File_name):
            return {'Books': [], 'Users': [], 'Transactions': []}
        
        with open(StorageManager.File_name, 'r') as f:
            return json.load(f)