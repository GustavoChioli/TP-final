from funciones import *
import pandas as pd

lista_registros = []

agregar = "si"
while agregar == "si":
    sensor_id = input("Ingrese un sensor_id: ")
    temperatura = input("Ingrese la temperatura del sensor: ")
    ubicacion = input("Ingrese en que planta esta el sensor: ")

    registros_raw = {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion":ubicacion
        }

    registros_clean = limpiar_registro_sensor(registros_raw)
    lista_registros.append(registros_clean)
    print (registros_clean)
    
    agregar = input("Desea agregar mas registros? indique 'si'").strip().lower()

df_sensores = pd.concat(lista_registros, ignore_index=True)

umbral_temperatura = pedir_float("Indique un umbral aceptable de temperatura: ")
sensores_alerta, promedio = generar_resumen_sensores(df_sensores, umbral_temperatura)

print("\n===== REPORTE FINAL =====")
print(f"Umbral de temperatura: {umbral_temperatura:.1f} °C")
print(f"Promedio global de la planta: {promedio:.2f} °C")
if sensores_alerta:
    print(f"Sensores en alerta ({len(sensores_alerta)}): {', '.join(sensores_alerta)}")
else:
    print("Ningún sensor superó el umbral.")