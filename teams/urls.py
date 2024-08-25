
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.vista_teams, name='vista_teams'),
    path('', views.vista_teams, name='teams'),
    path('acceso_formacion/', views.vista_teams, name='acceso_formacion'),
    path('teams/', views.teams_view, name='teams_view'),
    path('authorize/', views.authorize, name='authorize'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
    path('create_teams_event/', views.create_teams_event, name='create_teams_event'),
    path('gracias/', views.gracias_view, name='gracias'),
    path('teams/', views.teams_view, name='teams_view'),
    path('get_token/', views.get_token, name='get_token'),
]