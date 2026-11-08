import pandas as pd

valor_por_defecto ={
    "sensor_id": "desconocido",
    "temperatura": 0.0,
    "ubicacion": "Sin ubicacion"
}

def pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje).strip().replace(",", "."))
        except ValueError:
            print("Valor inválido. Ingrese un número (por ejemplo 30 o 30.5).")

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
    
    return registro_clean

def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura)->tuple:
    df = lista_sensores_limpios
    
    lista_sensores_alerta = df.loc[df["temperatura"] > umbral_temperatura, "sensor_id"].tolist()
    
    promedio_temperatura = df["temperatura"].mean()

    return(lista_sensores_alerta, promedio_temperatura)