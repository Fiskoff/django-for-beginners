from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_index),
    # Более конкретный маршрут должен быть объявлен выше, чем более абстрактный, общие маршрут
    path('about/contact/', views.get_contact),
    path('about/', views.get_about),
    # Параметры пути
    path('user/<str:name>/<int:age>/', views.get_user),
    path('user/<str:name>/', views.get_user),
    path('user/', views.get_user),
]