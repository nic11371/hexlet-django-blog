from django.urls import path
from hexlet_django_blog import views
from hexlet_django_blog.article import views as views_article

urlpatterns = [
    path('', views_article.index),
]
