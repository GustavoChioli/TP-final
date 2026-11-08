from .emisiones import calcular_emisiones_carbono


def obtener_metricas_consumo(registros: list) -> dict:
    """
    registros: [{"planta": "Planta Norte", "consumo_kwh": 1200.0}, ...]
    Una misma planta puede aparecer varias veces (historial).
    """
    consumo_por_planta = {}
    for r in registros:
        planta = r["planta"]
        consumo_por_planta[planta] = consumo_por_planta.get(planta, 0) + r["consumo_kwh"]

    emisiones_por_planta = {
        planta: calcular_emisiones_carbono(consumo)
        for planta, consumo in consumo_por_planta.items()
    }

    total_emisiones = sum(emisiones_por_planta.values())
    planta_mayor_consumo = (
        max(consumo_por_planta, key=consumo_por_planta.get)
        if consumo_por_planta else None
    )

    return {
        "total_emisiones": total_emisiones,
        "planta_mayor_consumo": planta_mayor_consumo,
        "emisiones_por_planta": emisiones_por_planta,
    }