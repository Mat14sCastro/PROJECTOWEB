from django.shortcuts import render,redirect
from .forms import CustomUserForm
from django.contrib.auth import login,authenticate


# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def catalogo(request):
    return render(request, 'core/catalogo.html')

def escopetas(request):
    return render(request, 'core/escopetas.html')

def lmg(request):
    return render(request, 'core/lmg.html')

def pistols(request):
    return render(request, 'core/pistols.html')

def revolver(request):
    return render(request, 'core/revolver.html')

def rifledeasalto(request):
    return render(request, 'core/rifledeasalto.html')

def sniper(request):
    return render(request, 'core/sniper.html')

def subfusiles(request):
    return render(request, 'core/subfusiles.html')

def td(request):
    return render(request, 'core/td.html')

def login(request):
    return render (request, 'core/login.html')


#REGISTRO DE USUARIO
def registro_user(request):
    data={'form':CustomUserForm()}
    if request.method == 'POST':
        formulario =CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save();
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(to='home')
    
    return render(request, "registration/registrar.html",data)


def checkout(request):
    return render(request,'core/checkout.html')


