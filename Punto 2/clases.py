import json

class StockInvalidoError(Exception):
    """Se lanza cuando se intenta asignar un stock negativo."""
    def __init__(self, valor, mensaje=None):
        self.valor = valor
        super().__init__(mensaje or f"Stock inválido: {valor}. No puede ser negativo.")


class DispositivoEcologico:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int):
        if valor < 0:
            raise StockInvalidoError(valor)
        self.__stock = valor

    def ficha_tecnica(self) -> str:
        return (f"Dispositivo: {self.nombre}\n"
                f"Precio: ${self.precio:,.2f}\n"
                f"Stock: {self.stock} unidades")

    def to_dict(self) -> dict:
        return {
            "tipo": type(self).__name__,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
        }


class PanelSolar(DispositivoEcologico):
    def __init__(self, nombre, precio, stock, potencia_watts: float, eficiencia: float):
        super().__init__(nombre, precio, stock)
        self.potencia_watts = potencia_watts
        self.eficiencia = eficiencia

    # Polimorfismo: misma firma que la clase base, comportamiento propio
    def ficha_tecnica(self) -> str:
        return (f"=== Panel Solar ===\n"
                f"{super().ficha_tecnica()}\n"
                f"Potencia: {self.potencia_watts} W\n"
                f"Eficiencia: {self.eficiencia:.1f}%")

    def to_dict(self) -> dict:
        datos = super().to_dict()
        datos["potencia_watts"] = self.potencia_watts
        datos["eficiencia"] = self.eficiencia
        return datos

class GestorInventario:
    def guardar_catalogo_json(self, lista_dispositivos: list, ruta_archivo: str):
        datos = [d.to_dict() for d in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)