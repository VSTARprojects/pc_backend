# Generated by Django 4.1.7 on 2023-02-26 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_laboratory_pathologists_alter_laboratory_upin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='pathologists',
            field=models.ManyToManyField(related_name='laboratory_pathologists', to='core.pathologist'),
        ),
        migrations.AlterField(
            model_name='laboratory',
            name='upin',
            field=models.CharField(default='<function uuid4 at 0x7f756b58a830>', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='pathologist',
            name='laboratory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pathologist_laboratory', to='core.laboratory'),
        ),
    ]