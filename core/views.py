from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, Order, OrderItem

# Create your views here.

def product(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "product.html", context)
 

class HomeView(ListView):
    model = Item
    template_name = "home.html"

def checkout(request):
    return render(request, "checkout.html")


class ProductDetailView(DetailView):
    model = Item
    template_name = "product.html"


def add_to_cart(request, slug):
    item = get_object_or_4ß4(Item, slug=slug)