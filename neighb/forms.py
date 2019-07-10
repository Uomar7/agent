from django import forms
from django.forms import TextInput, CharField, Textarea
from .models import Profile, Comment, Home
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        exclude = ["owner"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["house","posted"]
        widgets = {
            'comment':TextInput(attrs={
                'id':'comment',
                'placeholder':'Write A Review'
            })
        }
