from django.shortcuts import render
from django.views import View

from game.models.card import Card


class ConsultaTodasAsCartas(View):
    def get(self, request):
        cards = Card.objects.all()
        total_de_cartas = len(cards)
        context = {
            "resultados": cards,
            "total_de_cartas": total_de_cartas,
        }
        return render(request, 'todas_as_cartas/consulta_todas_as_cartas.html', context)