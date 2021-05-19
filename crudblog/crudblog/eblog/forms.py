from django import forms
from .models import Post, User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = [
            "title",
            "slug",
            "content",
            "status"
        ]


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password"
        ]
