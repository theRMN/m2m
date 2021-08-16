from django.views.generic import ListView
from articles.models import Article


class ArticleView(ListView):
    template_name = 'articles/news.html'
    queryset = Article.objects.all()
