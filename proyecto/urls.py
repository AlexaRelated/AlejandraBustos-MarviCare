from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  # Asegúrate de importar las vistas de blog
from inicio import views as inicio_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('inicio.urls')),
    path('', inicio_views.index, name='index'),  # Página de inicio
    path('login/', inicio_views.login_view_cuentas, name='login'),  
    path('logout/', inicio_views.logout_view, name='logout'),
    path('signup/', inicio_views.signup_view_cuentas, name='signup'),
    path('post/<int:pk>/', blog_views.article, name='post_detail'),  # Corrige la ruta aquí
    path('category/<str:category>/', blog_views.category_view, name='category'),
    path('crear_publicacion/', blog_views.crear_publicacion, name='crear_publicacion'),
    path('blog/', include('blog.urls')),  # Incluye las rutas de la aplicación blog
    path('inicio/', include('inicio.urls')),  # Incluye las rutas de la aplicación inicio
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
