from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
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

    class Meta:
        ordering = ('event_date_time',)


def __str__(self):
    return self.title