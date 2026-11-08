from django.shortcuts import render
from .metricas import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    # En un proyecto real, esto vendría de un modelo: Consumo.objects.values(...)
    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200.0},
        {"planta": "Planta Sur", "consumo_kwh": 950.5},
        {"planta": "Planta Norte", "consumo_kwh": 800.0},
        {"planta": "Planta Este", "consumo_kwh": 400.0},
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "total_emisiones": round(metricas["total_emisiones"], 2),
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "emisiones_por_planta": metricas["emisiones_por_planta"],
    }
    return render(request, "sustentabilidad/panel.html", contexto)