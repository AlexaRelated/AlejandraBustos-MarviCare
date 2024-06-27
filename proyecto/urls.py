from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inicio import views as inicio_views
from usuarios import views as usuarios_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_views.index, name='index'),  # Página de inicio
    path('usuarios/', include('usuarios.urls')), # URLs del módulo usuarios
    path('inicio/', include('inicio.urls')),  # URLs del módulo inicio
    path('login/', usuarios_views.login_view_cuentas, name='login'),  # URL para iniciar sesión
    path('registro/', usuarios_views.signup_view_cuentas, name='registro'),  # URL para registro
    path('logout/', usuarios_views.logout_view, name='logout'),  # URL para cerrar sesión
    path('post/<int:pk>/', blog_views.article, name='post_detail'),  
    path('category/<str:category>/', blog_views.category_view, name='category'),
    path('crear_publicacion/', blog_views.crear_publicacion, name='crear_publicacion'),
    path('blog/', include('blog.urls')),  # Incluye las URLs de blog al final para evitar conflictos
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
