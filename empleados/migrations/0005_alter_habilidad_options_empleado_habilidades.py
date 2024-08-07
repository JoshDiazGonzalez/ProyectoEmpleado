# Generated by Django 5.0.6 on 2024-06-29 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_rename_habilidades_habilidad'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='habilidad',
            options={'verbose_name': 'Habilidad', 'verbose_name_plural': 'Habilidades Empleados'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='empleados.habilidad'),
        ),
    ]
