from django.contrib import admin
from .models import Listing, Watchlist, Categories, Bid, User
# Register your models here.

admin.site.register(Listing)
admin.site.register(Watchlist)
admin.site.register(Categories)
admin.site.register(Bid)
admin.site.register(User)