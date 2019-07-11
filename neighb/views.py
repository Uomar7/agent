from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Profile, Home, Review
from .forms import ProfileForm, ReviewForm, HomeForm
from django.contrib.auth.models import User
# creating an api view for my models.
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer, HomeSerializer, ReviewSerializer
from rest_framework import status

def home(request):
    return render(request, 'all_temps/home.html')

@login_required(login_url="/accounts/login/")
def display(request):
    houses = Home.objects.all()
    return render(request, 'all_temps/hs.html',{"houses":houses})

@login_required(login_url="/accounts/login/")
@transaction.atomic
def profile(request,id):
    profile = Profile.objects.get(username = id)
    houses = profile.houses.all()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('profile',profile.id)

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request,'all_temps/profile.html', {"profile":profile,"houses":houses,"form":form})

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, format=None):
        all_Profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_Profiles, many=True)

        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)

        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)

        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(APIView):
    permission_classes = (IsAdminOrReadOnly)

    def get(self, request, format=None):
        all_comments = Comment.objects.all()
        serializers = ReviewSerializer(all_comments, many=True)

        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = ReviewSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Reaponse(serializers.data, status=status.HTTP_400_BAD_REQUEST)


class ReviewDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_comment(self, pk):
        try:
            return Review.objects.get(pk=pk)

        except Review.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        comment = self.get_comment(pk)
        serializers = ReviewSerializer(comment)

        return Response(serializers.data)

    def put(self, request, pk, format=None):
        comment = self.get_comment(pk)
        serializers = ReviewSerializer(comment, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HomeList(APIView):
    permission_classes = (IsAdminOrReadOnly)

    def get(self, request, format=None):
        all_houses = Home.objects.all()
        serializers = HomeSerializer(all_houses, many=True)

        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = HomeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(serializers.data,status=status.HTTP_400_BAD_REQUEST)


class HomeDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)

    def get_home(self, pk):
        try:
            return Home.objects.get(pk=pk)

        except Home.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        home = self.get_home(pk)
        serializers = HomeSerializer(profile)

        return Response(serializers.data)

    def put(self, request, pk, format=None):
        home = self.get_home(pk)
        serializers = HomeSerializer(home, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        home = self.get_home(pk)
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
