from django.urls import path
from . import views
app_name='catalogos'
urlpatterns = [
    # Organizacion URLs
    path('organizacion/', views.OrganizacionListView.as_view(), name='organizacion_list'),
    path('organizacion/create/', views.OrganizacionCreateView.as_view(), name='organizacion_create'),
    path('organizacion/update/<int:pk>/', views.OrganizacionUpdateView.as_view(), name='organizacion_update'),
    path('organizacion/delete/<int:pk>/', views.OrganizacionDeleteView.as_view(), name='organizacion_delete'),
    
    # Agrega rutas similares para Participante, Jugador, Torneo, etc.
]