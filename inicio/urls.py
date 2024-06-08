from django.contrib import admin
from django.urls import path
from proyecto import views as blog_views
from inicio import views as inicio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_views.index, name='index'),  # Página de inicio protegida
    path('login/', inicio_views.login_view_cuentas, name='login'),
    path('logout/', inicio_views.logout_view, name='logout'),
    path('signup/', inicio_views.signup_view_cuentas, name='signup'),
    path('post/<int:pk>/', inicio_views.article, name='post_detail'),
    path('category/<str:category>/', blog_views.category_view, name='category'),
    path('crear_publicacion/', blog_views.crear_publicacion, name='crear_publicacion'),
]

