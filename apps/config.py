from django.apps import AppConfig
from db.mongo_engine_client import connect_mongo  # Correct the import path
from db.pymongo_client import pymongo_client  # Correct the import path


class GlobalConfig(AppConfig):
    name = 'apps.config'

    def ready(self):
        # Import MongoDB clients
        print("connecting to mongo .....")
        connect_mongo()