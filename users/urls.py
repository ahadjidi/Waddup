from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

# Defines urls for most urls, also determines which view to use from views.py file
# based on the given url, also determines url name to be used in html
# templates when generating urls
urlpatterns = [
    #path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", views.EventList.as_view(), name="waddup_home"),
    path("users/", include("django.contrib.auth.urls")),
    path("users/signup/", views.SignUp.as_view(), name="signup"), 
    #path('happ-now/', views.EventList.as_view(), name = 'waddup_home'),
    #path('logout/', views.EventList.as_view(),name='waddup_home'),
    path('events/<slug:slug>/', views.EventDetail.as_view(), name = 'event_detail'),
    path('create/', views.AddEventView.as_view(), name = 'create_event'),
    path('map/', views.MapView.as_view(), name = 'map'),
    path('friends/', views.FriendList.as_view(), name = 'friends'),
    path('my_profile/', views.ProfileView.as_view(), name = 'profile'),
    #path('searchfriends', views.searchfriends, name='friend_search' )
    path('friends/',views.ProfileView.as_view(), name = 'searchbar'),
    path('events/<slug:slug>/edit', views.UpdateEventView.as_view(), name = 'update_event'),
    path('events/<slug:slug>/delete', views.DeleteEventView.as_view(), name = 'delete_event'),
    #path("signup/", views.SignUp.as_view(), name="signup"),
    ]