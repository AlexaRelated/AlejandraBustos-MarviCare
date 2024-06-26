from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name="index.html")),
    path('signup/', views.signup_view_cuentas, name='signup'),
    path('login/', views.login_view_cuentas, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),

]
