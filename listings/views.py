from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import Http404

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('home')  # redirect to home page after registration
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


# Contact View
def contact(request):
    return render(request, 'contact.html')


# CRUD Views - Listing Create, Retrieve, Update, Delete, List

def listing_retrieve(request, pk):
    try:
        listing = Listing.objects.get(id=pk)
    except Listing.DoesNotExist:
        raise Http404("Listing not found")
    return render(request, 'templates/listing_detail.html', {'listing': listing})


def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


# Home Page View
def home(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "base.html", context)


# Listing Create View
@login_required  # Only logged-in users can create a listing
def listing_create(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to home after creating a listing

    context = {
        "form": form
    }
    return render(request, "listing_create.html", context)


# Listing Update View
@login_required  # Only logged-in users can update a listing
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to home after updating the listing

    context = {
        "form": form
    }
    return render(request, "listing_update.html", context)


# Listing Delete View
@login_required  # Only logged-in users can delete a listing
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect("home")  # Redirect to home after deleting a listing
