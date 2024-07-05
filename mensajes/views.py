from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



class ChatView(TemplateView):
    template_name = 'usuarios/chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['connected_users'] = User.objects.all()
        context['room_name'] = self.kwargs['room_name']
        return context

@login_required
def private_chat(request, username):
    return render(request, 'usuarios/templates', {
        'other_user': username,
    })

@login_required
def get_users(request):
    users = User.objects.values('username')
    return JsonResponse({'users': list(users)})

def room(request, room_name):
    return render(request, 'mensajes/room.html', {
        'room_name': room_name
    })
