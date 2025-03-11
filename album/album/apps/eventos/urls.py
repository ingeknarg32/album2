from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('', views.lista_eventos, name='lista_eventos'),
    path('<int:id>/', views.detalle_evento, name='detalle_evento'),
]


