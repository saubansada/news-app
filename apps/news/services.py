from apps.news.models import NewsArticle

class NewsArticleService: 

    def __init__(self, article_model=NewsArticle):
        self.article_model = article_model

    def get_all_articles(self):
        return self.article_model.objects.all()

    def get_article_by_id(self, article_id):
        return self.article_model.objects.get(id=article_id)

    def create_article(self, title, content):
        return self.article_model.objects.create(title=title, content=content)

    def update_article(self, article_id, title, content):
        article = self.get_article_by_id(article_id)
        article.title = title
        article.content = content
        article.save()
        return article

    def delete_article(self, article_id):
        article = self.get_article_by_id(article_id)
        article.delete()
        return article