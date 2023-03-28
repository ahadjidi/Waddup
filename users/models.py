from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings


class CustomUser(AbstractUser):
    pass
    # add additional fields in here
    bio = models.TextField(default = 'This user has not yet created a bio.')
    
    def __str__(self):
        return self.username

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

    def get_absolute_url(self):
        return reverse('waddup_home')
    class Meta:
        ordering = ('event_date_time',)
    def __str__(self):
        return self.title
