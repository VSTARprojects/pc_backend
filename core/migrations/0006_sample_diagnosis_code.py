# Generated by Django 4.1.7 on 2023-02-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='diagnosis_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Diagnosis Code'),
        ),
    ]
