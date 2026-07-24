from django.urls import  path
from apps.crud import views

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),

]