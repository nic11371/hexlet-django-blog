from django.urls import path
from hexlet_django_blog import views
from hexlet_django_blog.article import views as views_article
from hexlet_django_blog.article.views import Article

urlpatterns = [
    path(
        '<str:tags>/<int:article_id>/',
        Article.as_view(),
        name='article',
        ),
]
