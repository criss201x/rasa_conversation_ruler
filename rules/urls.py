from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create', views.addCategoria),
    path ('read/<str:pk>', views.getCategoria),
    path ('update/<str:pk>', views.updateCategoria),
    path ('delete/<str:pk>', views.deleteCategoria),
]