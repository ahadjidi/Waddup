from django.db import models
from django.contrib.auth.models import User


# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

AGES = (
    (0, "18+"),
    (1, "21+"),
    (2, "All ages welcome")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete =models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default = 0)

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




## Sorts the results in event_date_time field in descending order 
class Meta:
    ordering = ['event_date_time']


def __str__(self):
    return self.title