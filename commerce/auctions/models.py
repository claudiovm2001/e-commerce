from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)
    st_bid = models.IntegerField()
    img = models.CharField(max_length=255)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}, {self.title}"

class Bid(models.Model):
    listing_id = models.IntegerField(default=-1)
    value = models.IntegerField(default=-1)

    def __str__(self):
        return f"{self.listing_id}, {self.value}"

class Comment(models.Model):
    listing_id = models.IntegerField()
    content = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.listing_id}, {self.content}"

class Watchlist(models.Model):
    listing_id = models.IntegerField()

    def __str__(self):
        return f"{self.listing_id}"

class Categories(models.Model):
    title = models.CharField(max_length=64)
    listing_id = models.IntegerField()