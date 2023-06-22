# Generated by Django 4.2.2 on 2023-06-21 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidoP', models.CharField(max_length=30)),
                ('apellidoM', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.IntegerField(max_length=11)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
    ]