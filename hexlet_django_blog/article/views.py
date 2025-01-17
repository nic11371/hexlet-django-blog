from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.views import View
from hexlet_django_blog.article.models import Article

# Create your views here.


# class Article_(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, 'articles/index.html', context={
#             'articles': f"Статья номер {self.kwargs['article_id']}. Тег {self.kwargs['tags']}",
#             })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article
        })
