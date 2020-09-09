"""django_journal URL Configuration
google.com

# oncom
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views
from journal import views as journal_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('journal/', include('journal.urls')),
    path('login',journal_views.login_user,name="login_user"),
    # path('logout',journal_views.logout_user,name="logout_user"),
    path('register',journal_views.register,name="register"),
    path('', views.index, name='index')
]
