from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_noticias, name="listado_noticias"),
    path('<int:id>/', views.detalle_noticia, name="detalle_noticia"),
]