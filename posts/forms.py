from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class PostForm(ModelForm):

    class Meta:
        model = Post
