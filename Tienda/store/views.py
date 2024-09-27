from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import gafas
<<<<<<< HEAD
from .forms import bodega,CreateProducts

=======
from users.forms import UserRegisterForm 
>>>>>>> aacf7767fbbfb486b47e8a83db329ee17a444d8e


@login_required
def index(request):
    return render(request, 'index.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#handles creation of new products 
def newProduct(request):
    return render(request, 'index.html')
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
<<<<<<< HEAD



=======
    
    
>>>>>>> aacf7767fbbfb486b47e8a83db329ee17a444d8e
