from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from principal.views import HomePageView
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('torneo/',include(('torneo.urls'), namespace='torneos')),
    path('catalogo/',include(('catalogo.urls'), namespace='catalogos')),
   
    path('api-auth/', include('rest_framework.urls')),
    # Otras rutas...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomePageView.as_view(), name='casa'), 
    path('accounts/', include('django.contrib.auth.urls')),
]
