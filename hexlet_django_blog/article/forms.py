from django.forms import ModelForm
from .models import Article
from django import forms


class ArticleForm(ModelForm):
    name = forms.CharField(max_length=100, required=True)
    body = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Article
        fields = ['name', 'body']
