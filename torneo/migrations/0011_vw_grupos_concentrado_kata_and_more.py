# Generated by Django 5.1.2 on 2024-11-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0010_gruposareas_torneo_torneo_nareas_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VW_Grupos_Concentrado_Kata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Grupo', models.IntegerField()),
                ('NombreG', models.CharField(max_length=100)),
                ('grupo', models.IntegerField()),
                ('Nombre_Grupo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vw_grupos_concentrado_kata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VW_Grupos_Concentrado_Kumite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Grupo', models.IntegerField()),
                ('NombreG', models.CharField(max_length=100)),
                ('grupo', models.IntegerField()),
                ('Nombre_Grupo', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'vw_grupos_concentrado_kumite',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VW_Grupos_Division_Kata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_id', models.IntegerField()),
                ('Categoria', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('TotalParticipantes', models.IntegerField()),
                ('Grupos', models.IntegerField()),
            ],
            options={
                'db_table': 'vw_grupos_por_division_kata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VW_Grupos_Division_Kumite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_id', models.IntegerField()),
                ('Categoria', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('TotalParticipantes', models.IntegerField()),
                ('Grupos', models.IntegerField()),
            ],
            options={
                'db_table': 'vw_grupos_por_division_kumite',
                'managed': False,
            },
        ),

    ]