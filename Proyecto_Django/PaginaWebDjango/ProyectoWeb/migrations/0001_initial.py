# Generated by Django 5.0.6 on 2024-06-06 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mensaje',
            fields=[
                ('id_mensaje', models.AutoField(db_column='idMensaje', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=100)),
                ('asunto', models.CharField(max_length=30)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
    ]
