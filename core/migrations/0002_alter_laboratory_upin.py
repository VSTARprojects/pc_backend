# Generated by Django 4.1.7 on 2023-02-26 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='upin',
            field=models.CharField(default='<function uuid4 at 0x7f516a22a830>', max_length=255, unique=True),
        ),
    ]
