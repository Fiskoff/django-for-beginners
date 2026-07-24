from django.urls import  path
from apps.crud import views

urlpatterns = [
    path('', views.index)
]