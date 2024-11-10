from rest_framework_mongoengine import serializers
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, IntField, DateTimeField, ListField
import datetime

class Comment(EmbeddedDocument):
    content = StringField()
    author = StringField()
    published_date = DateTimeField(default=datetime.datetime.utcnow)

class NewsArticle(Document):
    title = StringField()
    content = StringField()
    views = IntField(default=0)
    published_date = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(default=[])
    comments = ListField(required=False,null=True)
    author = StringField(null=False, default="-")
    source_url = StringField(null=True)

    meta = {
        'collection': 'news'  # Name of the MongoDB collection
    }