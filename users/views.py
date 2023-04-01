from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings

from .forms import CustomUserCreationForm, CreateEventForm, EditForm, CustomUserChangeForm
from .models import Event, CustomUser

# Redefines certain friendship views
try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User


from friendship.exceptions import AlreadyExistsError
from friendship.models import Block, Follow, Friend, FriendshipRequest

# Defines the majority of webpage views, including login, happening now, the 
# event detail page, edit/delete event pages, create event page, my profile page, 
# friend list view, map view, and certain functions requires by these views.
# Note: some views utilize forms in order to generate forms by default such as 
# signup form as well as the "add event" form. See users/forms.py for further
# information. 
# Note: all .html files / templates used can be found inside of the templates 
# directory or the friendship/templates directory.

# Utilizes CustomerUserCreationForm to generate page view, also uses built-in 
# CreateView to allow for implicit object creation using a form
class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

# Utilizes event.html template using list of events ordered by date / time,
# showing the soonest events first, also uses built-in ListView to allow for
# implicit object listing given a queryset, in this case the list of events 
# ordered by date / time
class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('event_date_time')
    template_name = 'events.html'

# Defines event detail page view, utilizes event_detail.html template to display
# event details correctly
class EventDetail(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'

# Utilizes CreateEventForm and create_event.html to generate page view for 
# creating an event, also uses built-in CreateView to allow for implicit
# object creation using a form
class AddEventView(generic.CreateView):
    form_class = CreateEventForm
    template_name = 'create_event.html'

# Utilizes EditForm and update_event.html to generate page view for 
# updating an already posted event, also uses built-in UpdateView to allow for
# automatic/implicit updating using a form
class UpdateEventView(generic.UpdateView):
    model = Event
    form_class = EditForm
    template_name = "update_event.html"
    # fields = ('title', 'event_date_time', 'event_type', 'desc', 'event_price','age')

# Utilizes built-in DeleteView and delete_event.html to allow ability to delete
# an event, redirected to home page upon success
class DeleteEventView(generic.DeleteView):
    model = Event
    template_name = "delete_event.html"
    success_url = reverse_lazy('waddup_home')

# Generates friend list view using simple friend.html template and built-in
# TemplateView
class FriendList(generic.TemplateView):
    template_name = 'friends.html'

# Generates my profile view using simple my_profile.html template and built-in
# TemplateView 
class ProfileView(generic.TemplateView):
    template_name = 'my_profile.html'

# Generates map view using simple map.html template and built-in
# TemplateView
class MapView(generic.TemplateView):
    template_name = 'map.html'


def get_friendship_context_object_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_NAME", "user")


def get_friendship_context_object_list_name():
    return getattr(settings, "FRIENDSHIP_CONTEXT_OBJECT_LIST_NAME", "users")

def view_friends(request, username, template_name="friendship/friend/user_list.html"):
    """View the friends of a user"""
    user = get_object_or_404(user_model, username=username)
    friends = Friend.objects.friends(user)
    return render(
        request,
        template_name,
        {
            get_friendship_context_object_name(): user,
            "friendship_context_object_name": get_friendship_context_object_name(),
            "friends": friends,
        },
    )

# Defines default map to be displayed on map.html page
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    #The Mapbox access token should really be stored in the Django settings file,
    # so i left a "TODO" note to handle that as a future step.
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, '_base.html',
                  { 'mapbox_access_token': mapbox_access_token })

