# pymongo_client.py

from pymongo import MongoClient

from config.settings import base

client = MongoClient(base.MONGO_DB_HOST, base.MONGO_DB_PORT)
    
    # Access the MongoDB database
pymongo_client = client[base.MONGO_DB_NAME]