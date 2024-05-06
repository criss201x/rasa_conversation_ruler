from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('iniciar_sesion/', views.signup),
    path('lista_categorias/', views.listaCategorias),
    path('logout/', views.salir),
    path('logear/', views.logear)
]