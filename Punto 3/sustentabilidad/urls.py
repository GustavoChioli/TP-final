from django.urls import path
from . import vistas

urlpatterns = [
    path("", vistas.vista_panel_sustentabilidad, name="panel_sustentabilidad"),
]