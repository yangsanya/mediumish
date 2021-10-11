from django.urls import path
from .views import Home, GetPost, GetAuthorInfo

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>', GetPost.as_view(), name='get_post'),
    path('author/<int:pk>', GetAuthorInfo.as_view(), name='get_author'),
]


