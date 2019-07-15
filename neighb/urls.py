from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^display/$',views.display, name='index'),
    url(r'^profile/(\d+)',views.profile,name="profile"),
    url(r'^search',views.search, name='search'),
    url(r'^add/$',views.add_home,name="add"),
    url(r'^single_house/(\d+)',views.single_house,name="single_house"),
    url(r'^api/comment/$',views.ReviewList.as_view()),
    url(r'^api/home/$',views.HomeList.as_view()),
    url(r'^api/profile/$',views.ProfileList.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
