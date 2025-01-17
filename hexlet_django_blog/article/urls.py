from django.urls import path
from hexlet_django_blog.article import views
# from hexlet_django_blog.article import views as views_article
# from hexlet_django_blog.article.views import Article_
# from hexlet_django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    # path(
    #     '<str:tags>/<int:article_id>/',
    #     Article_.as_view(),
    #     name='article',
    #     ),
    path('', views.IndexView.as_view(), name='articles_index'),
    path('<int:id>/', views.ArticleView.as_view(), name='articles_detail'),
]
