from django.urls import path
from .views import Home, GetPost, GetAuthorInfo, CreatePost, UpdatePost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>', GetPost.as_view(), name='get_post'),
    path('author/<int:pk>', GetAuthorInfo.as_view(), name='get_author'),
    path('author/<int:pk>', GetAuthorInfo.as_view(), name='get_author'),
    path('create-post/', CreatePost.as_view(), name='create_post'),
    path('update-post/<slug:slug>', UpdatePost.as_view(), name='update_post'),
    path('delete-post/<slug:slug>', DeletePost.as_view(), name='delete-post'),
]
