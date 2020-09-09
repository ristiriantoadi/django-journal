from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login',views.login,name="login"),
    # path('register',views.register,name="register"),
    # path('post',views.post,name="post"),
    path('add_post',views.add_post,name="add_post"),
    path('read_post',views.read_post,name="read_post"),
    path('delete_post',views.delete_post,name="delete_post"),
    path('edit_post',views.edit_post,name="edit_post"),
    path('logout',views.logout_user,name="logout_user")
    # path('logout',views.logout_user)
]