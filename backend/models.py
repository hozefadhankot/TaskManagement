from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client.task_manager

class Task:
    @staticmethod
    def create(data):
        return db.tasks.insert_one(data)

    @staticmethod
    def get_all():
        return list(db.tasks.find())

    @staticmethod
    def get(task_id):
        return db.tasks.find_one({'_id': task_id})

    @staticmethod
    def update(task_id, data):
        return db.tasks.update_one({'_id': task_id}, {'$set': data})

    @staticmethod
    def delete(task_id):
        return db.tasks.delete_one({'_id': task_id})
