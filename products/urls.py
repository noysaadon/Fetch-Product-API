from django import views
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
   path('', views.searchproduct ,name='getprodoct'),
   path('productdetails/', views.getproduct ,name='productdetails'),
   path('addproduct/',views.addproduct , name='addproduct'),
   path('ask_productlist/',views.ask_productlist ,name='ask_productlist'),
   path('productlist/', views.productlist , name='productlist')
]