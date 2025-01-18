from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse
from django.views import View
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.


# class Article_(View):

#     def get(self, request, *args, **kwargs):
#         return render(request, 'articles/index.html', context={
#             'articles': f"Статья номер {self.kwargs['article_id']}. 
# Тег {self.kwargs['tags']}",
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


class ArticleFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))
        messages.add_message(request, messages.ERROR, "Некорректные данные")
        return render(request, 'articles/create.html', {'form': form})


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, 'articles/update.html', {
                'form': form, 'article_id': article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))

        messages.add_message(request, messages.ERROR, "Некорректные данные")
        return render(
            request, 'articles/update.html', {
                'form': form, 'article_id': article_id})


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect(reverse('articles_index'))


# class CommentArticleView(View):
#     def post(self, request, *args, **kwargs):
#         form = CommentArticleForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 name = form.cleaned_data['content']
#                 )
#             comment.save()

#     def get(self, request, *args, **kwargs):
#         form = CommentArticleForm()
#         return render(request, 'comment.html', {'form': form})
