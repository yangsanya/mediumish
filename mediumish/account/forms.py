from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'bio', 'avatar']
        exclude = ()
        widgets = {
            'avatar': forms.FileInput(),
            'bio': forms.Textarea(),
        }
