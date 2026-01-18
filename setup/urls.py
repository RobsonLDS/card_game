from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("game/")),
    path("admin/", admin.site.urls),
    path("game/", include("game.urls")),
]
