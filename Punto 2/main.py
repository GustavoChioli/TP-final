from clases import * 

if __name__ == "__main__":
    catalogo = []

    # 1) Intento inválido en el constructor
    try:
        panel_malo = PanelSolar("Panel X", 150000, -5, 400, 21.5)
    except StockInvalidoError as e:
        print(f"Error capturado: {e}")

    # 2) Productos válidos
    panel1 = PanelSolar("Panel Solar 450W", 185000, 20, 450, 21.8)
    panel2 = PanelSolar("Panel Solar 550W", 240000, 10, 550, 22.4)
    catalogo.extend([panel1, panel2])

    # 3) Intento inválido sobre un objeto ya existente
    try:
        panel1.stock = -3
    except StockInvalidoError as e:
        print(f"Error capturado: {e}")

    print(panel1.ficha_tecnica())   # el stock sigue en 20

    # 4) Exportación de los productos válidos
    GestorInventario().guardar_catalogo_json(catalogo, "catalogo_ecotech.json")
    print("Catálogo guardado en catalogo_ecotech.json")