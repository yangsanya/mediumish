from django import forms
from .models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tags', 'text', 'time_to_read', 'image', 'is_published', ]

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'time_to_read': forms.NumberInput(),
            'image': forms.FileInput()

        }
