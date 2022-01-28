from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Watchlist
from django import forms

class NewListingForm(forms.Form):
    title = forms.CharField(label="Título")
    desc = forms.CharField(label="Descrição")
    st_bid = forms.IntegerField(label="Lance inicial")
    img = forms.CharField(label="Imagem")

def index(request):
    return render(request, "auctions/index.html", {
        "auctions": Listing.objects.filter(closed=False)
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):

    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            l = Listing(
                title = form.cleaned_data["title"],
                desc = form.cleaned_data["desc"],
                st_bid = form.cleaned_data["st_bid"],
                img = form.cleaned_data["img"]),
                #closed = False
            l.save()
        

    form = NewListingForm()
    return render(request, "auctions/create.html", {
        "form": form
    })

'''
def listings(request):
    return render(request, "auctions/listings.html", {
        "listings": Listing.objects.all()
    })
'''

def auction(request, auction_id):
    return render(request, "auctions/auction.html", {
        "auction": Listing.objects.get(id=auction_id)
    })

def close(request, auction_id):
    auction = Listing.objects.get(id=auction_id)
    auction.closed = True
    auction.save()

    return HttpResponseRedirect(reverse("index"))

def watchlist(request):
    keys = Watchlist.objects.all().values_list('listing_id', flat=True)

    watch = Listing.objects.filter(pk__in=keys)

    return render(request, "auctions/watchlist.html", {
        "watchlist": watch
    })

def watchlist_add(request, auction_id):
    item = Watchlist(listing_id = auction_id)
    item.save()
    return HttpResponseRedirect(reverse("index"))