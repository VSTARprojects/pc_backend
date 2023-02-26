from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.models import Patient
from core.serializers import PatientSerializer

@api_view(['GET'])
def getAllPatients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatient(request, id):
    patient = Patient.objects.get(id=id)
    serializer = PatientSerializer(patient)
    return Response(serializer.data)

@api_view(['POST'])
def addPatient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)