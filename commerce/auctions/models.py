from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    pass

    def __str__(self):
        pass

class Bid(models.Model):
    pass

    def __str__(self):
        pass

class Comment(models.Model):
    pass

    def __str__(self):
        pass