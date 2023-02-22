from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import Event

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'event_date_time', 'event_type', 'age', 'created_on')
    list_filter = ('event_type', "status")
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
