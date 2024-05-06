from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create', views.addMensajeRespuesta),
    path ('read/<str:pk>', views.getMensajeRespuesta),
    path ('update/<str:pk>', views.updateMensajeRespuesta),
    path ('delete/<str:pk>', views.deleteMensajeRespuesta),
]