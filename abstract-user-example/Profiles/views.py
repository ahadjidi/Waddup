from django.shortcuts import render
from .models import Profile
# Create your views here.
def my_profile(request):
    profile = Profile.objects.get(user = request.user)
    context = {'profile':profile}
    return render(request,'Profiles/myprofile.html',context)