from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('carrito/', views.carrito, name= "carrito"),
    path('catalogo/', views.catalogo, name= "catalogo"),
    path('escopeta/', views.escopetas, name= "escopeta"),
    path('lmg/', views.lmg, name= "lmg"),
    path('pistols/', views.pistols, name= "pistols"),
    path('revolver/', views.revolver, name= "revolver"),
    path('rifledeasalto/', views.rifledeasalto, name= "rifledeasalto"),
    path('sniper/', views.sniper, name= "sniper"),
    path('subfusiles/', views.subfusiles, name= "subfusiles"),
    path('td/', views.td, name= "td"),
    path('login/',views.login,name="login"),
    path('registro/',views.registro_user,name='registro_user'),
    path('checkout/',views.checkout,name="checkout"),
]