from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path ('create', views.addIntension),
    path ('read/<str:pk>', views.getIntension),
    path ('update/<str:pk>', views.updateIntension),
    path ('delete/<str:pk>', views.deleteIntension),
]