from injector import Provider, inject, Module, singleton, Injector
from .services import NewsArticleService
from .serializers import NewsArticleSerializer

class NewsModule(Module):
    def configure(self, binder):
        binder.bind(NewsArticleService, to=NewsArticleService, scope=singleton)

# Set up Injector
injector = Injector([NewsModule])