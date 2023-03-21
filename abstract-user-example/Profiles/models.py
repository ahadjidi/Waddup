from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    #object = None
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    bio = models.TextField()
    friends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='friends', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()
    def __str__(self):
        return str(self.user)
STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted')

)
class Relationship(models.Model):
    sender  = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name = 'sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name = 'receiver')
    status = models.CharField(max_length=8,choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
# Create your models here.
