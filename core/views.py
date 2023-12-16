from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

# Create your views here.

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Item
    template_name = "home.html"
    


def checkout(request):
    return render(request, "checkout.html")

def home(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home.html", context)