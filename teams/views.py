from django.shortcuts import redirect, render
from django import forms
from .models import AccesoFormacion, TeamsMeeting
from .forms import AccesoFormacionForm, YourForm
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.http import HttpResponse
from .models import TrainingSession  
from usuarios.models import User



def vista_teams(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            # Procesa el formulario
            form.save()
            return redirect('success_url')  # Redirige a una URL de éxito
    else:
        form = YourForm()

    return render(request, 'teams/teams.html', {'form': form})

def teams_view(request):
    # Implementa la lógica de la vista aquí
    return render(request, 'teams/acceso_formacion.html', {'form': forms.Form})


def acceso_formacion_view(request):
    meeting_url = None
    try:
        meeting_url = TeamsMeeting.objects.first().meeting_url
    except AttributeError:
        meeting_url = 'URL de la reunión no configurada'
    
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if AccesoFormacion.objects.filter(email=email).exists():
            return render(request, 'teams/teams.html', {'email': email, 'meeting_url': meeting_url})
        else:
            error_message = 'Lo sentimos, tu correo electrónico no tiene acceso a esta formación. Gracias.'
            return render(request, 'teams/acceso_formacion.html', {'error_message': error_message})
    else:
        form = AccesoFormacionForm()
        return render(request, 'teams/acceso_formacion.html', {'form': form})

def vista_teams(request):
    meeting_url = None
    try:
        meeting_url = TeamsMeeting.objects.first().meeting_url
    except AttributeError:
        meeting_url = 'URL de la reunión no configurada'
    
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if AccesoFormacion.objects.filter(email=email).exists():
            # Renderizar la página de 'teams' si el correo está registrado
            return render(request, 'teams/teams.html', {'email': email, 'meeting_url': meeting_url})
        else:
            # Mostrar mensaje de error si el correo no está registrado
            error_message = 'Lo sentimos, tu correo electrónico no tiene acceso a esta formación. Gracias.'
            return render(request, 'teams/acceso_formacion.html', {'error_message': error_message})
    else:
        # Mostrar el formulario inicialmente si no es una solicitud POST
        form = AccesoFormacionForm()
        return render(request, 'teams/acceso_formacion.html', {'form': form})

def gracias_view(request):
    return render(request, 'teams/gracias.html')

# permisos de Teams

def authorize(request):
    flow = Flow.from_client_secrets_file(
        'path/to/your/client_secret.json',
        scopes=settings.GOOGLE_API_SCOPES,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    request.session['state'] = state
    return redirect(authorization_url)

def oauth2callback(request):
    state = request.session['state']
    flow = Flow.from_client_secrets_file(
        'path/to/your/client_secret.json',
        scopes=settings.GOOGLE_API_SCOPES,
        state=state,
        redirect_uri=settings.GOOGLE_REDIRECT_URI
    )

    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)

    return redirect('create_teams_event')

def create_teams_event(request):
    if 'credentials' not in request.session:
        return redirect('authorize')

    credentials = Credentials(**request.session['credentials'])
    service = build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': 'Microsoft Teams Event',
        'description': 'A chance to hear more about Microsoft\'s developer products.',
        'start': {
            'dateTime': '2023-01-01T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2023-01-01T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'conferenceData': {
            'createRequest': {
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet'
                },
                'requestId': 'some-random-string'
            }
        },
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
    }

    event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    meeting_url = event.get('hangoutLink')

    return render(request, 'teams/teams.html', {'meeting_url': meeting_url})

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def get_token(request):
    # Implementa la lógica de la vista aquí
    return JsonResponse({'token': 'your_token_value'})