from django.urls import path
from .views import checkout,  ProductDetailView, HomeView



app_name = 'core'

urlpatterns = [
    # path('', HomeView.as_view(), name='home'),
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>', ProductDetailView.as_view(), name='product'),   
]