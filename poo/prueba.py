# Clase Padre
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        return f"El {self.marca} está encendido."

# Clase Hija (Hereda de Vehiculo)
class Coche(Vehiculo):
    def conducir(self):
        return f"Conduciendo el {self.marca} por la carretera."

# Instalación directa/Uso:
mi_coche = Coche("Toyota")
print(mi_coche.arrancar())  # Heredado
print(mi_coche.conducir()) # Propio