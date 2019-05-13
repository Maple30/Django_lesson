from django.urls import path

from . import views

urlpatterns = [
    path('', views.nothing, name='nothing'),
    path('index/', views.index, name='index'),
]