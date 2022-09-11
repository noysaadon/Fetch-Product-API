from django.db import models

class Product(models.Model):
    def __str__(self):  
        return self.title

    source_id = models.CharField(max_length=200, primary_key=True)
    source = models.CharField(max_length=15)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)


class FavoriteList(models.Model):

    def __str__(self):
        return self.email

    email = models.EmailField(primary_key=True)
    favorite_product = models.ManyToManyField(Product, through='FavoriteandProduct')


class FavoriteandProduct(models.Model):

    source_id = models.ForeignKey('Product', on_delete=models.CASCADE)
    email = models.ForeignKey('FavoriteList', on_delete=models.CASCADE)

    def __str__(self):
        return "{} ---> {}".format(self.source_id.__str__() , self.email.__str__())
