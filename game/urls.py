from django.urls import path

# Pagina Principal
from game.views.home import Home

# Total de Cartas
from game.views.todas_as_cartas.consulta_todas_as_cartas import ConsultaTodasAsCartas

urlpatterns = [

    # Pagina Principal
    path('', Home.as_view(), name="home"),

    # Total de Cartas
    path('todas_as_cartas/consulta_todas_as_cartas', ConsultaTodasAsCartas.as_view(), name="consulta_todas_as_cartas"),
    path('todas_as_cartas/consulta_todas_as_cartas/', ConsultaTodasAsCartas.as_view(), name="consulta_todas_as_cartas"),

]