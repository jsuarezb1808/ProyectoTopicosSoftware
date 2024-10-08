from django.urls import path,re_path
from . import views

app_name='users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('', views.user_login, name='index'),
]