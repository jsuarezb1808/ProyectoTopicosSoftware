from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
#premade user form created by django
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
#local
from .models import  user
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate 
from django.contrib import messages



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
            return redirect('users:login')
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
                return redirect('store:viewProduct')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, "title": "SumEye"})
def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #user is logged
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