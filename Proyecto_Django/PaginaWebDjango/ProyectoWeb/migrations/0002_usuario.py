# Generated by Django 5.0.6 on 2024-06-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('nombre', models.CharField(max_length=14)),
                ('contrasena', models.CharField(max_length=16)),
            ],
        ),
    ]
