# Generated by Django 5.1.2 on 2024-11-29 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0012_alter_jugador_coach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='coach',
            field=models.IntegerField(default=0),
        ),
    ]
