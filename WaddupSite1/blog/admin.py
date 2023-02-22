from django.contrib import admin

#Import models create in models.py file
from .models import Post
from .models import Event
from .models import Friend

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'event_date_time', 'event_type', 'age', 'created_on')
    list_filter = ('event_type', "status")
    search_fields = ['title', 'desc']
    prepopulated_fields = {'slug': ('title',)}

class FriendAdmin(admin.ModelAdmin):
    list_display = ('username', 'slug', 'name', 'status')
    list_filter = ('status',)
    search_fields = ['username', 'name']
    prepopulated_fields = {'slug':('username',)}




# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Friend, FriendAdmin)
