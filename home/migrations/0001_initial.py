# Generated by Django 5.0.6 on 2024-06-27 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(max_length=30)),
                ('subtitulo', models.CharField(max_length=50)),
            ],
        ),
    ]
