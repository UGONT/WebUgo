# Generated by Django 5.0.6 on 2024-06-06 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWeb', '0002_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contrasena',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
