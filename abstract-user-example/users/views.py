from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from .models import Event

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
    # fields = ('title', 'event_date_time', 'event_type', 'desc', 'event_price','age')