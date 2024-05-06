from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create', views.addMensajeIntension),
    path ('read/<str:pk>', views.getMensajeIntension),
    path ('update/<str:pk>', views.updateMensajeIntension),
    path ('delete/<str:pk>', views.deleteMensajeIntension),
]