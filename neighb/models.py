from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    id_no = models.IntegerField(max_length = 12)
    email = models.EmailField()
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='avatar/', blank=True)

    def __str__(self):
        return self.fname
    
    def save_profile(self):
        self.save()
    
    def delete_profile(self):
        self.delete()
    
    @classmethod
    def get_profiles(cls):
        all_profs = Profile.objects.all()
        return all_profs
    
    @classmethod
    def get_profile_by_id(cls,id):
        prof = Profile.objects.get(id=id)
        return prof

class Home(models.Model):
    hname = models.CharField(max_length=66)
    pic1 = models.ImageField(upload_to='hao/')
    pic2 = models.ImageField(upload_to='hao/')
    pic3 = models.ImageField(upload_to='hao/')
    location = models.CharField(max_length = 80)
    price = models.CharField(max_length = 80)
    description = models.TextField()
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='houses')

    def __str__(self):
        return  self.hname
    
    def save_home(self):
        self.save()
    
    def delete_home(self):
        self.delete()

class Review(models.Model):
    comment = models.CharField(max_length = 120)
    house = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='comments')
    posted = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

class Booking(models.Model):
    housename = models.CharField(max_length = 80)
    person = models.CharField(max_length = 80)
    location =  models.CharField(max_length = 80)
    email = models.CharField(max_length = 80)
    p_no = models.IntegerField(max_length= 12)

    def __str__(self):
        return self.housename

    def save_booking(self):
        self.save()
    
    def delete_booking(self):
        self.delete()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()