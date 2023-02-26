from django.urls import path
from . import views

urlpatterns = [
    path('patient/all/', views.getAllPatients),
    path('patient/add/', views.addPatient),
    path('patient/<int:id>/', views.getPatient)
]