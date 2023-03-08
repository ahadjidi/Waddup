from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import CustomUserCreationForm
from .models import Event, CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('event_date_time')
    template_name = 'events.html'

class EventDetail(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'

class AddEventView(generic.CreateView):
    model = Event
    template_name = 'create.html'
    fields = '__all__'
    #fields = ('title', 'event_date_time', 'event_type', 'desc', 'event_price','age')

class FriendList(generic.TemplateView):
    template_name = 'friends.html'

class ProfileView(generic.TemplateView):
    template_name = 'my_profile.html'

class MapView(generic.TemplateView):
    template_name = 'map.html'

# Friend Request and Sent Request views, may or may not need

class FriendRequests(generic.TemplateView):
    template_name = 'friend_requests.html'

class SentRequests(generic.TemplateView):
    template_name = 'sent_requests.html'

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    #The Mapbox access token should really be stored in the Django settings file,
    # so i left a "TODO" note to handle that as a future step.
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, '_base.html',
                  { 'mapbox_access_token': mapbox_access_token })