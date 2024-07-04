from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inicio import views as inicio_views
from usuarios import views as usuarios_views
import mensajes.routing  # Importa el módulo de routing de mensajes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),  # Página de inicio
    path('usuarios/', include('usuarios.urls')),  # URLs del módulo usuarios
    path('inicio/', include('inicio.urls')),  # URLs del módulo inicio
    path('login/', usuarios_views.login_view_cuentas, name='login'),  # URL para iniciar sesión
    path('registro/', usuarios_views.signup_view_cuentas, name='registro'),  # URL para registro
    path('logout/', usuarios_views.logout_view, name='logout'),  # URL para cerrar sesión
    path('mensajes/', include('mensajes.urls')),
    path('ws/', include(mensajes.routing.websocket_urlpatterns)),  # Incluye las rutas de WebSocket correctamente
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
