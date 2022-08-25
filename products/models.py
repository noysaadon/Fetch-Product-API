from sys import maxsize
from django.db import models

class Product(models.Model):

    def __str__(self):
        return self.title

    source_id = models.CharField(max_length=200)
    source = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    

class FavoriteList(models.Model):

    def __str__(self):
        return self.email

    email = models.EmailField(unique=True)
    favorite_product = models.ManyToManyField(Product)
