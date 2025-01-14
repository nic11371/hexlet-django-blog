from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class Article(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html', context={
            'articles': f"Статья номер {self.kwargs['article_id']}. Тег {self.kwargs['tags']}",
            })
