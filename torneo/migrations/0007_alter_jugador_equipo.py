# Generated by Django 5.1.2 on 2024-11-27 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_tipocompetencia'),
        ('torneo', '0006_alter_jugador_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores_equipo', to='catalogo.organizacion'),
        ),
    ]
