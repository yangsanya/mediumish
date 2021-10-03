from django.urls import path
from .views import Home, postview

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/', postview, name='postview')
]


