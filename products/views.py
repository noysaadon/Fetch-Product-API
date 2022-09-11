from http.client import BAD_REQUEST
import requests
from django.shortcuts import redirect, render
from products.models import Product , FavoriteList
from django.contrib import messages
import pdb


def searchproduct(request):
    global source
    global source_id
    if request.method =='POST':
        source = request.POST.get('source','')
        source_id = request.POST.get('source_id','')

        token = 'yblnoys829aljfy59'

        try:
            response = requests.get('https://ebazon-prod.herokuapp.com/ybl_assignment/'+ source + '/'+ source_id + '/' + token)
            ans = response.json()
            ans = ans['data']
            price = ans['price']
            title = ans['title']

            Product.objects.get_or_create(source = source, source_id = source_id, price=price , title=title)
            return redirect('productdetails')

        except Exception as e:  
            messages.error(request, "Opss... Check the deatils again. error message type : '%s'" % type(e))

    return render(request,'product/searchproduct.html')


def getproduct(request):
    desired_product = Product.objects.filter(source=source , source_id=source_id)
    return render(request ,'product/productdetails.html', {'desired_product': desired_product})


def addproduct(request):
    if request.method == 'POST':
        email = request.POST.get('email','')
        source = request.POST.get('source','')
        source_id = request.POST.get('source_id','')

        if Product.objects.filter(source = source ,source_id = source_id).exists():
            p = Product.objects.get(source = source ,source_id = source_id)
            
            if FavoriteList.objects.filter(email=email).exists():
                e= FavoriteList.objects.get_or_create(email=email)
            
            FavoriteandProduct.objects.filter(email= e).update_or_create(source_id = p)

        else:
            messages.error(request, "The product doesnt exsit in the DB. Please go to 'Search Product' to insert the product")
            return redirect('addproduct')
            
        return redirect('ask_productlist')

    return render(request,'product/addproduct.html')


def ask_productlist(request):
    global em
    if request.method == 'POST':
        em = request.POST.get('email','')

        return redirect('productlist')
    
    return render(request, 'product/ask_productlist.html')


def productlist(request):

    try:
        user = FavoriteList.objects.get(email=em)
        product_list = user.favorite_product.all()
    except FavoriteList.DoesNotExist:
        messages.error(request, "There isn't exist this email adrees. Please create your favorite list")
        product_list=None

    return render(request ,'product/productlistdetails.html', {'product_list':product_list})
