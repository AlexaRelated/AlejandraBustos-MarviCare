from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios import views as usuarios_views  # Importa las vistas de usuarios
from inicio import views as inicio_views  # Importa las vistas de inicio
from mensajes import views as mensajes_views  # Importa las vistas de mensajes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),  # Ruta para la página de inicio
    path('mensajes/', include('mensajes.urls')),  # Ruta para las URLs de mensajes
    path('redactar/', mensajes_views.redactar_mensaje, name='redactar_mensaje'),  # Ruta para redactar mensaje
    path('usuarios/', include('usuarios.urls')),  # Ruta para las URLs de usuarios
    path('login/', usuarios_views.login_view_cuentas, name='login'),  # Ruta para iniciar sesión
    path('registro/', usuarios_views.signup_view_cuentas, name='registro'),  # Ruta para registro
    path('logout/', usuarios_views.logout_view, name='logout'),  # Ruta para cerrar sesión
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

