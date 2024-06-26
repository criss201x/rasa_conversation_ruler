from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'login.html', { 'form' : UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password= request.POST['password1'] )
                user.save()
                login(request, user )
                return redirect('/lista_categorias/')
            except IntegrityError:
                return render(request, 'login.html', { 'form' : UserCreationForm, "error": "el usuario ya existe"})

        return render(request, 'login.html', { 'form' : UserCreationForm, "error": "las contraseñas no coinciden!"})

def home(request):
    return render(request, 'home.html')

def listaCategorias(request):
    return render(request, 'lista_categorias.html')

def salir(request):
    logout(request)
    return redirect('/')

def logear(request):    
    if request.method == 'GET':
        return render(request, 'logear.html', { 'form' : AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password= request.POST['password'] )
        if user is None:
            return render(request, 'logear.html', { 'form' : AuthenticationForm, "error": "usuario o contraseña incorrecta"})

        login(request, user )
        return redirect('/lista_categorias/')                