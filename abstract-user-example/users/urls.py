from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views


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

    #path("signup/", views.SignUp.as_view(), name="signup"),
    ]
