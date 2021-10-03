from django.urls import path
from .views import Home, GetPost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<slug:slug>', GetPost.as_view(), name='get_post')
]


