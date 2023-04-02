from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify

# Defines customer user model we utilized in order to add bio information and 
# login functionality.
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



# Defines our event class to store event data in database, works similarly to a 
# blog post in concept. Defines all necessary fields and options for certain 
# fields as well as necessary functions such as slug (url) generation based
# on the event title.

class Event(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    event_date_time = models.DateTimeField()

    PARTY = 'Party'
    CONCERT = 'Concert'
    COMEDY = 'Comedy Show'
    OTHER = 'Other'

    eighteen = "18+"
    twentyone = "21+"
    allwelcome = "All ages welcome"

    AGES = (
    (eighteen, "18+"),
    (twentyone, "21+"),
    (allwelcome, "All ages welcome")
    )   

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
    desc = models.TextField(default = 'No description has been provided for this event yet.')
    event_price = models.IntegerField(default = 0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    age = models.CharField(
        max_length=30,
        choices=AGES, 
        default=eighteen
        )
        
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default = 1)

    def get_absolute_url(self):
        return reverse('waddup_home')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('event_date_time',)   
