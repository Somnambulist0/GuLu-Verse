from django.urls import path
from . import views
from .views import views

urlpatterns = [
    path('', views.index0_view, name='index0'),
    path('main/', views.main_view, name='main'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('recommend_movies/', views.recommend_movies_view, name='recommend_movies'),
]


# urlpatterns = [
#     path('', views.index0_view, name='index0'),
#     path('main/', views.main_view, name='main'),
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('recommend-movies/', views.recommend_movies_view, name='recommend-movies')
#     path('recommend/', views.recommend_view, name='recommend'),
# ]