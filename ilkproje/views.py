#encoding: cp1254
from django.http import *
from django.shortcuts import render
from django.views.generic import TemplateView

"""class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, "index.html", context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"""

def post_list(request):
    return render(request, 'blog/post_list.html')

