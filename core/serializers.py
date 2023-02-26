from __future__ import annotations

from rest_framework import serializers

from core.models import Patient
from core.models import Sample


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
