from django.contrib import admin
from .models import Listing, Watchlist, Categories
# Register your models here.

admin.site.register(Listing)
admin.site.register(Watchlist)
admin.site.register(Categories)