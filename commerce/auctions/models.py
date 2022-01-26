from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=64)
    st_bid = models.IntegerField()
    img = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}, {self.desc}, {self.st_bid}, {self.img}"

class Bid(models.Model):
    pass

    def __str__(self):
        pass

class Comment(models.Model):
    pass

    def __str__(self):
        pass