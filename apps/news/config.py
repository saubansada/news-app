
from django.apps import AppConfig

from apps.config import GlobalConfig

class NewsConfig(GlobalConfig):
    name = 'apps.news'

    def ready(self):
        super().ready()
        
        import apps.news.injector
        # App-specific initialization logic
        print("News app initialization...")