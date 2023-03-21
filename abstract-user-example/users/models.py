from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ########Changes
    #User = settings.AUTH_USER_MODEL
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # friends = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='friends',blank=True)
    # updated = models.DateTimeField(auto_now = True)
    # created = models.DateTimeField(auto_now_add=True)




    ####################

    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    FRIENDS_LIST = []

    def __str__(self):
        return self.email

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

AGES = (
    (0, "18+"),
    (1, "21+"),
    (2, "All ages welcome")
)

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event_date_time = models.DateTimeField()

    PARTY = 'Party'
    CONCERT = 'Concert'
    COMEDY = 'Comedy Show'
    OTHER = 'Other'
    EVENT_TYPE_CHOICES = [
        (PARTY, 'Party'),
        (CONCERT, 'Concert'),
        (COMEDY, 'Comedy Show'),
        (OTHER, 'Other'),
    ]
    event_type = models.CharField(
        max_length=15,
        choices=EVENT_TYPE_CHOICES,
        default=PARTY,
    )

    updated_on = models.DateTimeField(auto_now=True)
    desc = models.TextField()
    event_price = models.IntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    age = models.IntegerField(choices=AGES, default=0)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse('waddup_home')
    class Meta:
        ordering = ('event_date_time',)


# class FriendList(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="user")
#     friends = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True,related_name="friends")
#
#     def __str__(self):
#         return self.user.username
#
#     def add_friend(self,account):
#         if not account in self.friends.all():
#             self.friends.add(account)
#             self.save()
#
#     def remove_friend(self,account):
#         if account in self.friends.all():
#             self.friends.remove(account)
#
#     def unfriend(self,removee):
#         remover_friends_list = self
#         remover_friends_list.remove_friend(removee)
#         friends_list = FriendList.objects.get(user=removee)
#         friends_list.remove_friend(self.user)
#
#     def is_mutual_friend(self,friend):
#         if friend in self.friends.all():
#             return True
#         return False
#
#
#
# class FriendRequest(models.Model):
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="sender")
#     receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
#     is_active = models.BooleanField(blank=True,null=False,default = True)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.sender.username
#
#     def accept(self):
#         receiver_friend_list = FriendList.objects.get(user = self.receiver)
#         if receiver_friend_list:
#             receiver_friend_list.add_friend(self.sender)
#             sender_friend_list = FriendList.objects.get(user=self.sender)
#             if sender_friend_list:
#                 sender_friend_list.add_friend(self.receiver)
#                 self.is_active = False
#                 self.save()
#
#     def decline(self):
#         self.is_active = False
#         self.save()
#
#     def cancel(self):
#         self.is_active = False
#         self.save()



def __str__(self):
    return self.title