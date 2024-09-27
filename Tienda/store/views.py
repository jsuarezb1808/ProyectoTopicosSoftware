from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import gafas
from .forms import bodega,CreateProducts


#handles creation of new products 
def newProduct(View):
    def post(self,request):
        form=forms.CreateTask(request.POST)
        if form.is_valid():

#handles view of individual products
def viewProduct(view):
    def get(self,**kwargs):
        pass

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



