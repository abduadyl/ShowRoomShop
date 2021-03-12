from django.db import models
from myprofile.models import Profile

class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=9, decimal_places=2)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product/')


