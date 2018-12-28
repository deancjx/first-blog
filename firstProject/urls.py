#encoding: cp1254

from django.contrib import admin
from django.conf.urls import *
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ilkproje import views
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('ilkproje.urls')),
    #url(r'^$', views.HomePageView.as_view()),
    #url(r'^about', views.AboutPageView.as_view())

]

