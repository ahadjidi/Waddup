from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Event

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username",]


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'event_date_time', 'event_type', 'age', 'created_on')
    list_filter = ('event_type', "status")
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
# Register your models here.
