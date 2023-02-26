from django.db import models

class Patient(models.Model):
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    NOT_SAY = "N"

    SEXES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other"),
        (NOT_SAY, "Rather not say"),
    )

    first_name = models.CharField(max_length=255, null=True, verbose_name="First Name")
    last_name = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Last Name"
    )
    sex = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="Sex", choices=SEXES
    )
    dob = models.DateField(verbose_name="Date of birth", blank=True, null=True)

    def __str__(self):
        try:
            first_name = self.first_name or ""
            last_name = self.last_name or ""
            full_name = f"{first_name} {last_name}".strip()
        except:
            full_name = 'Not Specified'
        return full_name or None