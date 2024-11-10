from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework import serializers
from .models import NewsArticle, Comment

class CommentSerializer(DocumentSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'author', 'published_date')

class NewsArticleSerializer(DocumentSerializer):
    class Meta:
        model = NewsArticle  # Ensure correct model reference
        fields = ('title', 'content', 'views', 'title', 'comments', 'tags', 'author', 'source_url', 'published_date')
        extra_kwargs = {
            'comments': {'required': False},
            'tags': {'required': False}, 
            "source_url": { "required": False}
        }
        
    comments = CommentSerializer(many=True, required=False)
    tags = serializers.ListField(required=False)