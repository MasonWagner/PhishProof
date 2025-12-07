from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class_list/', views.class_list, name='class_list'),
    path('class/<int:pk>/', views.class_description, name='class_description'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]