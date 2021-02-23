#Define URL patterns for my_blog

from django.urls import path

from . import views

app_name = 'my_blog'
urlpatterns = [
    #Home page
    path('', views.index, name='index')
]