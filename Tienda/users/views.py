from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
#premade user form created by django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#local
from .models import  user
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from store.models import Wishlist
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('index')
            else:
                messages.error(request, 'Credenciales inválidas.')
        else:
            messages.error(request, 'Error en el formulario.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'SumEye'})


@login_required
def wishlist_view(request):
    user_wishlist = Wishlist.objects.filter(User=request.user).first()
    return render(request, 'wishlist.html', {'wishlist': user_wishlist})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('tasks:home')
    else:
        form=AuthenticationForm()

    return render(request,'users/login.html',{'form':form})

def logout_view(request):
    if (request.method=='POST'):
        logout(request)
        return redirect('users:login')
    
