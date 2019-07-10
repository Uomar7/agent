from rest_framework import serializers
from .models import Profile, Review, Home

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("username")

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        exclude = ("owner")

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("posted","house")
