import pandas as pd

valor_por_defecto ={
    "sensor_id": "desconocido",
    "temperatura": 0.0,
    "ubicacion": "Sin ubicacion"
}

def limpiar_registro_sensor(registro_raw:dict)->dict:
    registro_clean = pd.DataFrame([registro_raw])
    
    registro_clean = registro_clean.reindex(columns=valor_por_defecto.keys())
    registro_clean = registro_clean.replace(r"^\s*$", pd.NA, regex=True)

    registro_clean["sensor_id"] = registro_clean["sensor_id"].str.strip()    
    try:
        registro_clean["temperatura"] = pd.to_numeric(registro_clean["temperatura"])
    except ValueError:
        registro_clean["temperatura"] = pd.to_numeric(
            registro_clean["temperatura"].str.replace(r"[^0-9.\-]", "", regex=True),
            errors="coerce"
            )
    registro_clean = registro_clean.fillna(valor_por_defecto)
    
    print (registro_clean)

sensor_id = input("Ingrese un sensor_id: ")
temperatura = input("Ingrese al temperatura del sensor: ")
ubicacion = input("Ingrese en que planta esta el sensor: ")

registros_raw = {
    "sensor_id": sensor_id,
    "temperatura": temperatura,
    "ubicacion":ubicacion
    }

limpiar_registro_sensor(registros_raw)