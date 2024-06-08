from django.urls import path
from . import views as inicio_views

urlpatterns = [
    path('', inicio_views.index, name='index'),  # Página de inicio de inicio
    path('login/', inicio_views.login_view_cuentas, name='login'),
    path('logout/', inicio_views.logout_view, name='logout'),
    path('signup/', inicio_views.signup_view_cuentas, name='signup'),
]
