# Generated by Django 5.1.2 on 2024-11-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_tipocompetencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='agrupacion',
            field=models.IntegerField(default=0),
        ),
    ]