# Generated by Django 4.1.7 on 2023-02-26 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_laboratory_pathologists'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='laboratory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_laboratory', to='core.laboratory'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='patients',
            field=models.ManyToManyField(blank=True, related_name='user_patients', to='core.patient'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Last Name'),
        ),
    ]