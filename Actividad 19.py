class RegistroDuplicadoError(Exception):
    pass
class Galleta:
    def __init__(self, nombre, precio, peso):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        if peso <= 0:
            raise ValueError("El peso debe ser mayor que 0.")
        self.nombre = nombre
        self.precio = precio
        self.peso = peso
    def mostrar_info(self):
        return f"Galleta: {self.nombre} | Precio: Q{self.precio:.2f} | Peso: {self.peso}g"