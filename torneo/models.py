from django.db import models

from catalogo.models import Categoria, Deporte, Organizacion, TipoParticipante, TipoTorneo, TipoCompetencia

# Modelo para Torneo
class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoTorneo, on_delete=models.CASCADE, related_name='torneos')
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE, related_name='torneos')
    nareas = models.IntegerField(default=0)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return self.nombre

class AreasTorneo(models.Model):
    nombre = models.CharField(max_length=100)
    torneo = models.ForeignKey('Torneo', on_delete=models.CASCADE, related_name='areas')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.torneo.nombre}'

class GruposAreas(models.Model):
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey('AreasTorneo', on_delete=models.CASCADE, related_name='grupos')
    torneo = models.ForeignKey('Torneo', on_delete=models.CASCADE, related_name='grupos_torneo', default=0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.area.nombre}'

class GraficaTorneo(models.Model):
    nombre = models.CharField(max_length=100)
    torneo = models.ForeignKey('Torneo', on_delete=models.CASCADE, related_name='graficas')
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.torneo.nombre}'

# Modelo de Participante, puede ser un equipo o una escuela
class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoParticipante, on_delete=models.CASCADE, related_name='participantes')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='participantes', null=True, blank=True)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return self.nombre
    
class ParticipacionTorneo(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    fecha_participacion = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('participante', 'torneo')

    def __str__(self):
        return f"{self.participante.nombre} en {self.torneo.nombre}"
    
# Modelo para Jugador, si el Participante es un equipo, puede tener jugadores
class Jugador(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='jugadores_participante')
    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateTimeField(default=None)  
    equipo = models.ForeignKey(Organizacion,  on_delete=models.CASCADE, related_name='jugadores_equipo', null=True, blank=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    estatura = models.DecimalField(max_digits=5, decimal_places=2)  # en metros, ej: 1.75
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # en kilogramos, ej: 70.5
    tipo = models.ForeignKey(TipoParticipante, on_delete=models.CASCADE, related_name='jugadores')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='jugadores', null=True, blank=True)
    competencia = models.ForeignKey(TipoCompetencia, on_delete=models.CASCADE, related_name='jugadores')
    coach=models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nombre} - {self.equipo.nombre}'

# Modelo para Partido entre Participantes
class Partido(models.Model):
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='partidos')
    equipo_local = models.ForeignKey(Participante, related_name='partidos_local', limit_choices_to={'tipo__nombre': 'Equipo'}, on_delete=models.CASCADE)
    equipo_visitante = models.ForeignKey(Participante, related_name='partidos_visitante', limit_choices_to={'tipo__nombre': 'Equipo'}, on_delete=models.CASCADE)
    resultado_local = models.IntegerField(null=True, blank=True)
    resultado_visitante = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField()

    def __str__(self):
        return f'{self.equipo_local.nombre} vs {self.equipo_visitante.nombre}'

# Modelo para Clasificación de los Participantes en un Torneo
class Clasificacion(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='clasificaciones')
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE, related_name='clasificaciones')
    puntos = models.IntegerField(default=0)
    partidos_jugados = models.IntegerField(default=0)
    victorias = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    goles_a_favor = models.IntegerField(default=0)
    goles_en_contra = models.IntegerField(default=0)
    diferencia_goles = models.IntegerField(default=0)
    anotaciones = models.IntegerField(default=0)
    faltas = models.IntegerField(default=0)
    tarjetas_amarillas = models.IntegerField(default=0)
    tarjetas_rojas = models.IntegerField(default=0)

    def __str__(self):
        return f'Clasificación de {self.participante.nombre} en {self.torneo.nombre}'



class VW_Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100) 
    fecha_nacimiento = models.DateTimeField(default=None)  
    sexo = models.CharField(max_length=10)
    estatura = models.DecimalField(max_digits=5, decimal_places=2)  # en metros, ej: 1.75
    peso = models.DecimalField(max_digits=5, decimal_places=2)  # en kilogramos, ej: 70.5
    categoria_id = models.IntegerField()
    Grado = models.CharField(max_length=100)
    tipo_id = models.IntegerField()
    Categoria = models.CharField(max_length=100)
    competencia_id = models.IntegerField()
    Competencia = models.CharField(max_length=100)
    coach=models.IntegerField()
    equipo_id =  models.IntegerField()
    Escuela = models.CharField(max_length=100)

    class Meta:
        managed=False
        db_table='vw_jugador'

class VW_Grupos_Division_Kata(models.Model):
    tipo_id = models.IntegerField()
    Categoria = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    TotalParticipantes = models.IntegerField()
    Grupos = models.IntegerField()

    class Meta:
        managed=False
        db_table='vw_grupos_por_division_kata'

class VW_Grupos_Division_Kumite(models.Model):
    tipo_id = models.IntegerField()
    Categoria = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    TotalParticipantes = models.IntegerField()
    Grupos = models.IntegerField()

    class Meta:
        managed=False
        db_table='vw_grupos_por_division_kumite'

class VW_Grupos_Concentrado_Kata(models.Model):
    Id_Grupo= models.IntegerField()
    NombreG = models.CharField(max_length=100)
    grupo = models.IntegerField()
    Nombre_Grupo = models.CharField(max_length=100)

    class Meta:
        managed=False
        db_table='vw_grupos_concentrado_kata'

class VW_Grupos_Concentrado_Kumite(models.Model):
    Id_Grupo= models.IntegerField()
    NombreG = models.CharField(max_length=100)
    grupo = models.IntegerField()
    Nombre_Grupo = models.CharField(max_length=100)

    class Meta:
        managed=False
        db_table='vw_grupos_concentrado_kumite'

class VW_Horarios(models.Model):
    hora = models.CharField(max_length=100)

    class Meta:
        managed=False
        db_table='vw_horario'