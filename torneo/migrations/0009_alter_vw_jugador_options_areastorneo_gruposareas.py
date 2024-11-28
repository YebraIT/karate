# Generated by Django 5.1.2 on 2024-11-28 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0008_vw_jugador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vw_jugador',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='AreasTorneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('torneo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='torneo.torneo')),
            ],
        ),
        migrations.CreateModel(
            name='GruposAreas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='torneo.areastorneo')),
            ],
        ),
    ]