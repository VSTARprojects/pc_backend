from __future__ import annotations
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
import uuid
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
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        first_name = self.first_name or ''
        last_name = self.last_name or ''
        full_name = f'{first_name} {last_name}'.strip()
        return full_name or None

    def get_full_name(self):
        first_name = self.first_name or ''
        last_name = self.last_name or ''
        full_name = f'{first_name} {last_name}'.strip()
        return full_name


class Sample(models.Model):
    BIOPSY = 'B'
    SURGICAL_RESECTION = 'SR'
    OTHER = 'O'

    TYPE_CHOICES = (
        (BIOPSY, 'biopsy'),
        (SURGICAL_RESECTION, 'surgical resection'),
        (OTHER, 'Other')
    )

    BLOOD = 'B'
    TISSUE = 'T'
    URINE = 'U'
    STOOL = 'S'
    FLUID = 'F'
    OTHER = 'O'

    ORIGIN_CHOICES = (
        (BLOOD, 'blood'),
        (TISSUE, 'tissue'),
        (URINE, 'urine'),
        (STOOL, 'stool'),
        (FLUID, 'fluid'),
        (OTHER, 'Other')
    )

    patient = models.ForeignKey(
        'core.Patient',
        related_name='sample_patient',
        on_delete=models.PROTECT,
    )
    pathologists = models.ManyToManyField(
        'core.Pathologist',
        related_name='sample_pathologists',
    )
    laboratory = models.ForeignKey(
        'core.Laboratory',
        related_name='sample_laboratory',
        on_delete=models.PROTECT,
    )
    date_collected = models.DateTimeField(
        verbose_name='Date of collection', blank=True, null=True)
    diagnosis_code = models.CharField(
        max_length=8, blank=True, null=True, verbose_name='Diagnosis Code')
    type = models.CharField(
        max_length=50,
        blank=True, null=True, verbose_name='Type', choices=TYPE_CHOICES,
    )
    origin = models.CharField(
        max_length=50,
        blank=True, null=True, verbose_name='Site of Origin', choices=ORIGIN_CHOICES,
    )
    symptoms = models.CharField(max_length=800, blank=True)
    comments = models.CharField(max_length=800, blank=True)

    # def __str__(self):
    #     return f"{self.patient.get_full_name()}-{self.pathologist.get_full_name()}-{self.id}"


class Location(models.Model):
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    pin_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        if self.latitude and self.longitude:
            return f"({self.latitude}, {self.longitude})"
        return str(self.id)


class Laboratory(models.Model):
    upin = models.CharField(
        max_length=255, default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=255, verbose_name='Name')
    address = models.ForeignKey(
        "core.Location", on_delete=models.CASCADE, null=True)
    # admin_id = models.ForeignKey(
    #     'core.Pathologist',
    #     related_name='laboratory_admin',
    #     on_delete=models.PROTECT,
    # )
    pathologists = models.ManyToManyField(
        'core.Pathologist',
        blank=True,
        related_name='laboratory_pathologists'
    )

    def __str__(self):
        return self.name


class Pathologist(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Last Name',
    )
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField(
        verbose_name="Email Address", null=True, blank=True, max_length=255
    )
    laboratory = models.ForeignKey(
        'core.Laboratory',
        related_name='pathologist_laboratory',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    patients = models.ManyToManyField(
        'core.Patient',
        related_name='pathologist_patients'
    )

    def __str__(self):
        first_name = self.first_name or ''
        last_name = self.last_name or ''
        full_name = f'{first_name} {last_name}'.strip()
        return full_name or None

    def get_full_name(self):
        first_name = self.first_name or ''
        last_name = self.last_name or ''
        full_name = f'{first_name} {last_name}'.strip()
        return full_name


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    first_name = models.CharField(max_length=255, verbose_name='First Name')
    last_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name='Last Name',
    )
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    laboratory = models.ForeignKey(
        'core.Laboratory',
        related_name='user_laboratory',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    patients = models.ManyToManyField(
        'core.Patient',
        blank=True,
        related_name='user_patients'
    )

    def __str__(self):
        return self.email

    def get_full_name(self):
        first_name = self.first_name or ''
        last_name = self.last_name or ''
        full_name = f'{first_name} {last_name}'.strip()
        return full_name

    # solve the foreign key problems for pathologist and lab
    # chicken egg
