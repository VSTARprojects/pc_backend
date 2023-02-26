from __future__ import annotations

from rest_framework import serializers

from core.models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id', 'first_name', 'last_name',
            'dob', 'phone_number', 'sex',
        )


class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'


class PathologistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pathologist
        fields = '__all__'


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
