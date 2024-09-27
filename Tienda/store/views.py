from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import gafas

#handles creation of new products 
def newProduct(View):
    def get(self,request):
        pass
    def post(self,request):
        pass

#handles view of individual products
def viewProduct(view):
    def get(self,request):
        pass

#handles deletion of new products
def deleteProduct(view):
    def get(self,request):
        pass

#handles updates of products
def updateProduct(view):
    def get(self,request):
        pass

#handles the process to add on a whislist a product 
def wishlistProduct():
    def post(self,request):
        pass
    
    
def index(request):
    return render(request, 'index.html')

    

