# urls.py (inside your app, e.g., news)

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.news.models import NewsArticle
from apps.news.views import NewsArticleViewSet

router = DefaultRouter()
router.register(r'news', NewsArticleViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]
#router.register(r'news_articles/(?P<news_article_pk>[^/.]+)/comments', CommentViewSet, basename='comment')
