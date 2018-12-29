from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('',views.post_list, name='post_list'),
]
