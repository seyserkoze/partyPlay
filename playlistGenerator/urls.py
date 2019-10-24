from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authorize', views.authorize, name='authorize'),
    path('callback', views.callback, name='callback')
]