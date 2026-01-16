from django.urls import path
from game.views.home import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
]