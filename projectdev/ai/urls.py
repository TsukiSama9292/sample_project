from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/trigger/', views.trigger, name='trigger'),
    path('api/another/', views.another_view, name='another_view'),
]