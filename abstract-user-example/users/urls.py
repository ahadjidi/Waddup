from django.urls import path

from . import views


urlpatterns = [
    path('happ-now/', views.EventList.as_view(), name = 'waddup_home'),
    path('logout/', views.EventList.as_view(),name='waddup_home'),
    path('<slug:slug>/', views.EventDetail.as_view(), name = 'event_detail'),
    path("signup/", views.SignUp.as_view(), name="signup"),
    ]
