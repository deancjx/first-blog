#encoding: cp1254
from django.http import *
from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView
from django.utils import timezone

"""class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html", context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"""

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'blog/post_list.html', {"posts":posts})

