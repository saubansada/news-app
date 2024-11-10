from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from apps.news.models import NewsArticle
from apps.news.serializers import CommentSerializer, NewsArticleSerializer

class NewsArticleViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer

    # class CommentViewSet(viewsets.ModelViewSet):
    #     serializer_class = CommentSerializer   

    #     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #     def get_queryset(self):   

    #         news_article_id = self.kwargs['news_article_pk']
    #         return Comment.objects.filter(news_article=news_article_id)

    #     def perform_create(self, serializer):
    #         serializer.save(news_article=self.get_object())