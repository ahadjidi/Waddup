from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Event


# CustomUser creation form, requests user to input username, email, and bio
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",'bio')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email",'bio')

# Custom event creation form that specifies input format for event date and time
# data in order to ensure proper storage in database, also defines fields required
# by event creation form
class CreateEventForm(forms.ModelForm):
    event_date_time = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M', 
                                    help_text='Enter date and time with the following format: "YYYY-MM-DD HH:MM"  NOTE: Time is on a 24hr clock, so 6PM is 18:00, for example.')
    class Meta:
        model = Event
        fields = ('title', 'event_date_time', 'event_type', 'desc','event_price','age')

# Custom event edit form that specifies input format for event date and time
# data in order to ensure proper storage in database, also defines fields required
# by event edit form / fields to edit
class EditForm(forms.ModelForm):
    event_date_time = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M', 
                                    help_text='Enter date and time with the following format: "YYYY-MM-DD HH:MM"  NOTE: Time is on a 24hr clock, so 6PM is 18:00, for example.')
    class Meta:
        model = Event
        fields = ('title', 'event_date_time', 'event_type', 'desc','event_price','age')
