from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login',views.login,name="login"),
    # path('register',views.register,name="register"),
    path('post',views.post,name="post"),
    path('add_post',views.add_post,name="add_post"),
    path('logout',views.logout_user,name="logout_user")
    # path('logout',views.logout_user)
]