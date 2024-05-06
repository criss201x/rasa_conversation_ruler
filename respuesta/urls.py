from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create', views.addRespuesta),
    path ('read/<str:pk>', views.getRespuesta),
    path ('update/<str:pk>', views.updateRespuesta),
    path ('delete/<str:pk>', views.deleteRespuesta),
]