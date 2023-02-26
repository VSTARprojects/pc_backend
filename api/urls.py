from __future__ import annotations

from django.urls import include
from django.urls import path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'samples', views.SampleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
