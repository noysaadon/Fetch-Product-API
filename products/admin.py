from django.contrib import admin
from .models import FavoriteList, Product ,FavoriteandProduct

admin.site.register(Product)
admin.site.register(FavoriteList)
admin.site.register(FavoriteandProduct)
