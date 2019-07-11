from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^display/$',views.display, name='index'),
    url(r'^profile/(\d+)',views.profile,name="profile"),
    url(r'^api/comment/$',views.ReviewList.as_view()),
    url(r'^api/home/$',views.HomeList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
]
