# Generated by Django 4.1.7 on 2023-02-26 18:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_laboratory_admin_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='upin',
            field=models.CharField(default=uuid.uuid4, max_length=255, unique=True),
        ),
    ]
