from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    #path("listings", views.listings, name="listings"),
    path("auction/<int:auction_id>", views.auction, name="auction"),
    path("close/<int:auction_id>", views.close, name="close"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist_add/<int:auction_id>", views.watchlist_add, name="watchlist_add")
]
