from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import *
from django import forms

class NewListingForm(forms.Form):
    title = forms.CharField(label="Título")
    st_bid = forms.IntegerField(label="Lance inicial")
    img = forms.CharField(label="Imagem", required=False)

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
                desc = request.POST["desc"],
                st_bid = form.cleaned_data["st_bid"],
                img = form.cleaned_data["img"])
            l.save()

            select = request.POST['category']
            if select != 0:
                category = Categories(title = select, listing_id= l.id)
                category.save()
        

    form = NewListingForm()
    categories = Categories.objects.all().values_list('title', flat=True).distinct()

    return render(request, "auctions/create.html", {
        "form": form, "categories": categories
    })

'''
def listings(request):
    return render(request, "auctions/listings.html", {
        "listings": Listing.objects.all()
    })
'''

def auction(request, auction_id):
    in_list = Watchlist.objects.filter(listing_id = auction_id, owner=request.user.id).exists
    comments = Comment.objects.filter(listing_id = auction_id)
    start = Listing.objects.get(id=auction_id)
    highest = start.st_bid

    surpassed = Bid.objects.filter(listing_id = auction_id).exists()

    if surpassed:
        new = Bid.objects.get(listing_id=auction_id)
        highest = new.value

    return render(request, "auctions/auction.html", {
        "auction": Listing.objects.get(id=auction_id),
        "exists": in_list,
        "comments": comments,
        "highest": highest
    })

def close(request, auction_id):
    auction = Listing.objects.get(id=auction_id)
    auction.closed = True
    auction.save()

    return HttpResponseRedirect(reverse("index"))

def watchlist(request):
    keys = Watchlist.objects.filter(owner=request.user.id).values_list('listing_id', flat=True)
    #keys = Watchlist.objects.all().values_list('listing_id', flat=True)

    watch = Listing.objects.filter(pk__in=keys)

    return render(request, "auctions/watchlist.html", {
        "watchlist": watch
    })

def watchlist_add(request, auction_id):
    is_duplicate = Watchlist.objects.filter(listing_id = auction_id, owner=request.user.id).exists()

    if is_duplicate == True:
        return redirect('index')    

    item = Watchlist(listing_id = auction_id, owner=request.user.id)
    item.save()
    return redirect('index')

def watchlist_remove(request, auction_id):
    Watchlist.objects.filter(listing_id = auction_id, owner=request.user.id).delete()

    return redirect('index')

def categories(request):
    names = Categories.objects.all().values_list('title', flat=True).distinct()

    return render(request, "auctions/categories.html", {
        "names" : names
    })

def category(request, name):
    '''
    data = Categories.objects.filter(title = name)
    keys = data.objects.all().values_list('listing_id', flat=True)
    content = Listings.objects.filter(pk__in=keys)

    return render(request, "auctions/category.html", {
        "content": content, "title": name
    })
    '''

    keys = Categories.objects.all().filter(title = name).values_list('listing_id', flat=True)
    content = Listing.objects.filter(pk__in=keys)

    return render(request, "auctions/category.html", {
        "content": content, "title": name
    })

def comment(request, auction_id):
    if request.method == "POST":
        data = request.POST["content"]
        text = Comment(listing_id=auction_id, content=data)
        text.save()

        return redirect('index')

def bid(request, auction_id):
    if request.method == "POST":
        data = request.POST["value"]
        old = Listing.objects.get(id=auction_id)
        highest = old.st_bid
        

        in_database = Bid.objects.filter(listing_id=auction_id).exists()

        if in_database == True:
            old = Bid.objects.get(listing_id=auction_id)
            highest = old.value

            if int(data) > highest :
                new = Bid(listing_id=auction_id, value=data)
                old.delete()
                new.save()       
        
        return redirect('index')