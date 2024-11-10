
from django.apps import AppConfig

from apps.config import GlobalConfig

class UsersConfig(GlobalConfig):
    name = 'apps.users'

    def ready(self):
        super().ready()
        # App-specific initialization logic
        print("Users app initialization...")