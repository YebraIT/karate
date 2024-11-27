# Generated by Django 5.1.2 on 2024-11-26 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
        ('torneo', '0002_jugador_participante_alter_jugador_equipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugador',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='catalogo.categoria'),
        ),
        migrations.AddField(
            model_name='jugador',
            name='tipo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='catalogo.tipoparticipante'),
            preserve_default=False,
        ),
    ]