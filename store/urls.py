from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('posts/', views.posts, name = "posts"),
    path('store/', views.store, name = "store"),
    path('post/<int:post_id>', views.post_detail, name = "post_detail"),#new
    path('createpost', views.createPost, name = "createpost"),
]