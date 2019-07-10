from django import forms
from django.forms import TextInput, CharField, Textarea
from .models import Profile, Review, Home
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]

class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        exclude = ["owner"]

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["house","posted"]
        widgets = {
            'comment':TextInput(attrs={
                'id':'comment',
                'placeholder':'Write A Review'
            })
        }
