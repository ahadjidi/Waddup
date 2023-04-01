from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Event

# Allows admins to add CustomUser objects as well as Event objects from the admin
# page, based on given form data from users/forms.py

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]

# Defines the information displayed about events as well as info when creating
# event from admin page, such as prepopulating slug field based on the title
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'event_date_time', 'event_type', 'age', 'created_on')
    list_filter = ('event_type', "status")
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
# Register your models here.
