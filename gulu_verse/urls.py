"""
URL configuration for gulu_verse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView





urlpatterns = [
    path('jn189/', admin.site.urls),
    path('', views.index0, name='index0'),
    path('main/', views.main, name='main'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='index0'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)