from django import forms
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import gafas
from . import forms



home='store:view'

#handles creation of new products 
def newProduct(request):
    if request.method == "POST":
        form = forms.CreateProducts(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store:viewProducts')
    else:
        form = forms.CreateProducts()
    return render(request,'newProduct.html',{'form': form})


#handles view of individual products

def viewProduct(request):
    if request.method == "GET":
        Gafas=gafas
        return render(request,'store:viewProduct.html',Gafas)
    else:
        pass
    return render(request,'store:viewProduct.html')

def viewProducts(request):
    if request.method == "GET":
        Gafas=gafas
        return render(request,'viewProduct.html',{'gafas':Gafas})
    else:
        pass
    return render(request,'viewProduct.html',{"Gafas":gafas})



def detailProduct(request,id):
    def get(request):
        product=gafas.objects.get(ItemId=id)
        return render (request,'store/productDetail.html',{'product':product})

#handles deletion of new products
def deleteProduct(view):
    def get(self,**kwargs):
        pass

def updateProduct(request, id):
    product = gafas.objects.get(ItemId=id)
    if request.method == 'POST':
        form = forms.CreateProducts(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = forms.CreateProducts(instance=product)
    return render(request, 'store/newProduct.html', {'form': form})

def purchaseProduct(request,id):
    def post(self,request,id):
        product=gafas.objects.get(ItemId=id)
        

#handles updates of products


#handles the process to add on a whislist a product 
def wishlistProduct(request, id):
    product = get_object_or_404(gafas, ItemId=id)
   
    user_wishlist, created = wishlist.objects.get_or_create(User=request.user)
   
    if product not in user_wishlist.ItemsId.all():
        user_wishlist.ItemsId.add(product)
 
    return redirect('store:productDetail', id=id)
 
def purchaseProduct():
    pass

def cart(request):
    return render(request, 'store:cart.html')

def transactionPanel(request):
    return render(request, 'store:transaction.html')



