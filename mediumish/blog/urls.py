from django.urls import path
from .views import Home, GetPost, GetAuthorInfo, CreatePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>', GetPost.as_view(), name='get_post'),
    path('author/<int:pk>', GetAuthorInfo.as_view(), name='get_author'),
    path('author/<int:pk>', GetAuthorInfo.as_view(), name='get_author'),
    path('create-post/', CreatePost.as_view(), name='create_post'),
]
