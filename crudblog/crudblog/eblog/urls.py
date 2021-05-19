from .views import PostList, PostDetail, UpdatePost, CreatePost, DeletePost, CreateUser
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('register/', CreateUser.as_view(), name='register-user'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('posts/', CreatePost.as_view(), name='add-post'),
    path('posts/<int:pk>/', UpdatePost.as_view(), name='update-post'),
    path('posts/<int:pk>/delete', DeletePost.as_view(), name='delete-post'),

]
