from rest_framework import generics, viewsets
from core.models import Patient
from core.serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
