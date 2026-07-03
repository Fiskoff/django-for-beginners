from django.urls import path, include
from . import views


product_patterns = [
    path("", views.products),
    path("new/", views.new),
    path("top/", views.top),
    path("comment/", views.top),
    path("question/", views.top),
]

urlpatterns = [
    path('', views.get_index),
    # Более конкретный маршрут должен быть объявлен выше, чем более абстрактный, общие маршрут
    path('about/contact/', views.get_contact),
    path('about/', views.get_about),
    # Параметры пути
    path('user/<str:name>/<int:age>/', views.get_user),
    path('user/<str:name>/', views.get_user),
    path('user/', views.get_user),
    # Подключение инкапсулированных путей
    path('products/<int:id>/', include(product_patterns)),
]