from django.urls import path
from .views import SmartLiteLoginView, SmartLiteLogoutView

urlpatterns = [
    path('login/', SmartLiteLoginView.as_view(), name='login'),
    path('logout/', SmartLiteLogoutView.as_view(), name='logout'),
    # Rutas para otras vistas
]