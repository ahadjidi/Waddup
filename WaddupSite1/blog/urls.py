from . import views
from django.urls import path

urlpatterns = [
    ## path('', views.PostList.as_view(), name='home'),
    ##Takes empty string and returns result gerneated from PostList view (list of posts for homepage)
    ## path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    ##General expression for PostDetail views, resolves slug(string of ASCII letters and nums),
    ##Uses <> to capture values from URL and return equivalent post detail page
    path('', views.EventList.as_view(), name='home'),
    path('<slug:slug>/', views.EventDetail.as_view(), name = 'event_detail'),
    path('friends', views.FriendList.as_view(), name='friends'),
    path('<slug:slug>/', views.FriendDetail.as_view(), name = 'friend_detail'),
    ##Adapted the above code for our use (event stream)
]