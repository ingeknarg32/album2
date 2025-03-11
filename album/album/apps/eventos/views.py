from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Evento

def lista_eventos(request):
    eventos = Evento.objects.all().order_by('fecha')
    return render(request, "eventos/lista_eventos.html", {"eventos": eventos})

def detalle_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(request, "eventos/detalle_evento.html", {"evento": evento})


