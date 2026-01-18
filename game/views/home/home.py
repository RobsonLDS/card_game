from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        systems = []
        systems.append({
            "title": "Coliseu",
            "desc": "Batalhas rápidas para testar suas cartas.",
            "badge": "Batalha",
            "url": "coliseu",  # nome de url (vamos criar depois)
            "enabled": True,
        })
        systems.append({
            "title": "Abertura de Pacotes",
            "desc": "Abra pacotes e obtenha novas cartas.",
            "badge": "Recompensas",
            "url": "pacotes",
            "enabled": True,
        })
        systems.append({
            "title": "Fortalecimento",
            "desc": "Evolua cartas repetidas e aumente atributos.",
            "badge": "Upgrades",
            "url": "fortalecimento",
            "enabled": True,
        })
        systems.append({
            "title": "Coleção",
            "desc": "Veja suas cartas e monte decks.",
            "badge": "Cartas",
            "url": "colecao",
            "enabled": False,  # exemplo: ainda não implementado
        })
        systems.append({
            "title": "Todas as cartas",
            "desc": "Lista de todas as cartas.",
            "badge": "Cartas",
            "url": "todas_as_cartas/consulta_todas_as_cartas",
            "enabled": True,  # exemplo: ainda não implementado
        })
        return render(request, "home/home.html", {"systems": systems})