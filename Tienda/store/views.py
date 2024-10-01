from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import gafas
from . import forms

home='store:view'
#handles creation of new products 
def newProduct(View):
    def post(self,request):
        form=forms.CreateProducts(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect(home)
        else:
            form=forms.CreateProducts()
        return render(request,'store/newProduct.html',{'form':form})

#handles view of individual products
def viewProduct(request):
    def get(request):
        Gafas=gafas
        return render(request,'store/viewProduct.html',Gafas)

def detailProduct(request,id):
    def get(request):
        product=gafas.objects.get(ItemId=id)
        return render (request,'store/productDetail.html',{'product':product})

def purchaseProduct(request,id):
    def post(self,request,id):
        product=gafas.objects.get(ItemId=id)
        

#handles deletion of new products
def deleteProduct(view):
    def get(self,**kwargs):
        pass

#handles updates of products
def updateProduct(view):
    def get(self,**kwargs):
        pass

#handles the process to add on a whislist a product 
def wishlistProduct():
    def post(self,request):
        pass



