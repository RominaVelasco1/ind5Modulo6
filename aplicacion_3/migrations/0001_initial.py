# Generated by Django 4.2.3 on 2023-07-22 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registroUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
                ('ciudad', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=8)),
                ('creacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]