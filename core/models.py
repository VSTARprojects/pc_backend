from __future__ import annotations

from django.db import models


class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'
    NOT_SAY = 'N'

    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
        (NOT_SAY, 'Rather not say'),
    )

    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Last Name',
    )
    sex = models.CharField(
        max_length=1, blank=True, null=True, verbose_name='Sex', choices=SEX_CHOICES,
    )
    dob = models.DateField(verbose_name='Date of birth', blank=True, null=True)
    phone_number = models.CharField(max_length=15, default='9393938345')

    def __str__(self):
        first_name = self.first_name or ''
        last_name = self.last_name or ''
        full_name = f'{first_name} {last_name}'.strip()
        return full_name or None


class Sample(models.Model):
    pid = models.ForeignKey(
        'core.Patient',
        related_name='patient',
        on_delete=models.PROTECT,
    )
    date_collected = models.DateTimeField(
        verbose_name='Date of collection', blank=True, null=True)
    diagnosis_code = models.CharField(
        max_length=8, blank=True, null=True, verbose_name='Diagnosis Code')
