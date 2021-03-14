from django.db import models
from myprofile.models import ProfileCustomer
from main.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(ProfileCustomer, on_delete=models.CASCADE, related_name='cartitem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cartitem')
    amount = models.PositiveIntegerField(default=1)

class Cart(models.Model):
    products = models.ManyToManyField(CartItem)
    user = models.OneToOneField(ProfileCustomer, on_delete=models.CASCADE, related_name='cart')



