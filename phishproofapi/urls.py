from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('class_list/', views.class_list, name='class_list'),
    path('class/<int:pk>/', views.class_description, name='class_description'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name="logout"),
    path('class/<int:class_id>/enroll/', views.enroll_class, name='enroll_class'),
    path('challenge_list/', views.challenge_list, name='challenge_list'),
    path('challenge/<int:pk>/', views.challenge_description, name='challenge_description'),
    path('challenge/<int:challenge_id>/start/', views.start_challenge, name='start_challenge'),

]