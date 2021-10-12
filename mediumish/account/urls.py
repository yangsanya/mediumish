from django.urls import path
from .views import login_page, register_page, logoutUser, edit_profile

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('edit_profile/', edit_profile, name='edit_profile')
]
