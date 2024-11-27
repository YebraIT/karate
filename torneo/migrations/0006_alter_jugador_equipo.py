# Generated by Django 5.1.2 on 2024-11-27 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_tipocompetencia'),
        ('torneo', '0005_jugador_coach_jugador_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='equipo',
            field=models.ForeignKey(blank=True, limit_choices_to={'tipo__nombre': 'Equipo'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores_equipo', to='catalogo.organizacion'),
        ),
    ]