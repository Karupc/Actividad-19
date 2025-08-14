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
class GalletaChispas(Galleta):
    def __init__(self, nombre, precio, peso, cantidad_chispas):
        super().__init__(nombre, precio, peso)
        if cantidad_chispas < 0:
            raise ValueError("La cantidad de chispas no puede ser negativa.")
        self.cantidad_chispas = cantidad_chispas
    def mostrar_info(self):
        return super().mostrar_info() + f" | Chispas: {self.cantidad_chispas}"
class Relleno:
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno
    def describir_relleno(self):
        return f"Relleno de {self.sabor_relleno}"
class GalletaRellena(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)
    def mostrar_info(self):
        return super().mostrar_info() + f" | {self.describir_relleno()}"
nventario = []
def buscar_galleta(nombre):
    return next((g for g in inventario if g.nombre.lower() == nombre.lower()), None)
def menu():
    while True:
        print("\n--- MENÚ GALLETAS ---")
        print("1.- Registrar galleta básica")
        print("2.- Registrar galleta con chispas")
        print("3.- Registrar galleta rellena")
        print("4.- Listar galletas")
        print("5.- Buscar por nombre")
        print("6.- Eliminar por nombre")
        print("7.- Salir")
        opcion = input("Seleccione opción: ")
        match opcion:
            case "1":
                try:
                    nombre = input("Nombre: ")
                    if buscar_galleta(nombre):
                        raise RegistroDuplicadoError("Ya existe una galleta con ese nombre.")
                    precio = float(input("Precio: "))
                    peso = float(input("Peso (g): "))
                    inventario.append(Galleta(nombre, precio, peso))
                    print("Galleta registrada.")
                except ValueError as e:
                    print(f"Error: {e}")
                except RegistroDuplicadoError as e:
                    print(f"Error: {e}")
            case "2":
                try:
                    nombre = input("Nombre: ")
                    if buscar_galleta(nombre):
                        raise RegistroDuplicadoError("Ya existe una galleta con ese nombre.")
                    precio = float(input("Precio: "))
                    peso = float(input("Peso (g): "))
                    chispas = int(input("Cantidad de chispas: "))
                    inventario.append(GalletaChispas(nombre, precio, peso, chispas))
                    print("Galleta con chispas registrada.")
                except ValueError as e:
                    print(f"Error: {e}")
                except RegistroDuplicadoError as e:
                    print(f"Error: {e}")
            case "3":
                try:
                    nombre = input("Nombre: ")
                    if buscar_galleta(nombre):
                        raise RegistroDuplicadoError("Ya existe una galleta con ese nombre.")
                    precio = float(input("Precio: "))
                    peso = float(input("Peso (g): "))
                    sabor = input("Sabor del relleno: ")
                    inventario.append(GalletaRellena(nombre, precio, peso, sabor))
                    print("Galleta rellena registrada.")
                except ValueError as e:
                    print(f"Error: {e}")
                except RegistroDuplicadoError as e:
                    print(f"Error: {e}")