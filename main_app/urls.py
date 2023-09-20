from django.urls import path
from . import views

urlpatterns = [
    path('', views.index0_view, name='index0'),
    path('main/', views.main_view, name='main'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
