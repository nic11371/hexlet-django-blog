from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormEditView, ArticleFormDeleteView
# from hexlet_django_blog.article import views as views_article
# from hexlet_django_blog.article.views import Article_
# from hexlet_django_blog.article.views import IndexView, ArticleView

urlpatterns = [
    # path(
    #     '<str:tags>/<int:article_id>/',
    #     Article_.as_view(),
    #     name='article',
    #     ),
    path('', IndexView.as_view(), name='articles_index'),
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='articles_update'),
    path('<int:id>/', ArticleView.as_view(), name='articles_detail'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='articles_delete')
]
