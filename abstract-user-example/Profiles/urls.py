from django.urls import path
from .views import my_profile

urlpatterns = [
    path('myprofile/',my_profile,name ='my-profile-view'),
]