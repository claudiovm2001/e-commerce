from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)
    st_bid = models.IntegerField()
    img = models.CharField(max_length=64)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}, {self.title}"

class Bid(models.Model):
    pass

    def __str__(self):
        pass

class Comment(models.Model):
    pass

    def __str__(self):
        pass

class Watchlist(models.Model):
    listing_id = models.IntegerField()

    def __str__(self):
        return f"{self.listing_id}"

class Categories(models.Model):
    title = models.CharField(max_length=64)
    listing_id = models.IntegerField()