from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    slug = models.SlugField()
    short_description = models.CharField(max_length=255)
    long_description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('core:product', kwargs= {
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart(self):
        return reverse('core:remove-from-cart', kwargs={
            'slug': self.slug
        })

    # sku = models.CharField(max_length=255)
    # weight = models.FloatField()
    # cart_description = models.CharField(max_length=255)

    # thumbnail = models.ImageField(upload_to='thumbnails/')
    # image = models.ImageField(upload_to='products/')
    # stock = models.FloatField()
    # live = models.BooleanField(default=True)
    # location = models.CharField(max_length=255)
    # warehouse = models.CharField(max_length=255)
  

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)  
    ordered = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    shipping_fees = models.PositiveIntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    delivery_date = models.DateTimeField(blank=True, null=True)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return self.user.username

# class OrderDetail(models.Model):
#     detail_id = models.AutoField(primary_key=True, editable=False)
#     detail_order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     #detail_product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     detail_name = models.CharField(max_length=255)
#     detail_price = models.DecimalField(max_digits=10, decimal_places=2)
#     detail_sku = models.CharField(max_length=255)
#     detail_quantity = models.IntegerField()