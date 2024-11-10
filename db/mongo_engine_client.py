# mongoengine_client.py

import mongoengine as me
from django.conf import settings

def connect_mongo():
    if not me.connection:
        me.connect(
            db=settings.MONGO_DB_NAME,
            host=settings.MONGO_DB_HOST,
            port=settings.MONGO_DB_PORT
        )