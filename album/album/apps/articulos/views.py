from django.shortcuts import render
from .models import Noticia
from django.shortcuts import get_object_or_404

def listado_noticias(request):
    noticias = Noticia.objects.filter(publicada=True).order_by('-fecha_publicacion')
    return render(request, "articulos/listado_noticias.html", {"noticias": noticias})
def detalle_noticia(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, "articulos/detalle_noticia.html", {"noticia": noticia})