# Generated by Django 5.1.2 on 2024-11-13 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='catalogo.categoria')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='catalogo.organizacion')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='catalogo.tipoparticipante')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('paterno', models.CharField(max_length=100)),
                ('materno', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10)),
                ('estatura', models.DecimalField(decimal_places=2, max_digits=5)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('equipo', models.ForeignKey(limit_choices_to={'tipo__nombre': 'Equipo'}, on_delete=django.db.models.deletion.CASCADE, related_name='jugadores', to='torneo.participante')),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torneos', to='catalogo.deporte')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torneos', to='catalogo.tipotorneo')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado_local', models.IntegerField(blank=True, null=True)),
                ('resultado_visitante', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField()),
                ('equipo_local', models.ForeignKey(limit_choices_to={'tipo__nombre': 'Equipo'}, on_delete=django.db.models.deletion.CASCADE, related_name='partidos_local', to='torneo.participante')),
                ('equipo_visitante', models.ForeignKey(limit_choices_to={'tipo__nombre': 'Equipo'}, on_delete=django.db.models.deletion.CASCADE, related_name='partidos_visitante', to='torneo.participante')),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidos', to='torneo.torneo')),
            ],
        ),
        migrations.CreateModel(
            name='GraficaTorneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='graficas', to='torneo.torneo')),
            ],
        ),
        migrations.CreateModel(
            name='Clasificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.IntegerField(default=0)),
                ('partidos_jugados', models.IntegerField(default=0)),
                ('victorias', models.IntegerField(default=0)),
                ('empates', models.IntegerField(default=0)),
                ('derrotas', models.IntegerField(default=0)),
                ('goles_a_favor', models.IntegerField(default=0)),
                ('goles_en_contra', models.IntegerField(default=0)),
                ('diferencia_goles', models.IntegerField(default=0)),
                ('anotaciones', models.IntegerField(default=0)),
                ('faltas', models.IntegerField(default=0)),
                ('tarjetas_amarillas', models.IntegerField(default=0)),
                ('tarjetas_rojas', models.IntegerField(default=0)),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasificaciones', to='torneo.participante')),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clasificaciones', to='torneo.torneo')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipacionTorneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_participacion', models.DateField(auto_now_add=True)),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.participante')),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torneo.torneo')),
            ],
            options={
                'unique_together': {('participante', 'torneo')},
            },
        ),
    ]