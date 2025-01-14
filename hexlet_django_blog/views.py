from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request):
        return redirect('article', tags='python', article_id=42)


def about(request):
    return render(request, 'about.html')
