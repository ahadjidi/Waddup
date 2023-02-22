from django.views import generic

from .models import Post
from .models import Event
from .models import Friend


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    ## the (-) before -created_on signifies the latest post would be at 
    ## the top
    template_name = 'events.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class EventList(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('event_date_time')
    template_name = 'events.html'

class EventDetail(generic.DetailView):
    model = Event
    template_name = 'event_detail.html'

class FriendList(generic.ListView):
    queryset = Friend.objects.filter(status=1).order_by('-name')
    template_name = 'friends.html'

class FriendDetail(generic.DetailView):
    model = Friend
    template_name = 'friend_detail.html'
