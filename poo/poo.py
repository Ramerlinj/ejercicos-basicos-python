# 1. ABSTRACCIÓN: Clase base para cualquier servicio
class Servicio:
    def __init__(self, nombre_plan):
        self.nombre_plan = nombre_plan
        # 2. ENCAPSULAMIENTO: Precio base privado
        self.__precio_base = 9.99 

    def obtener_info(self):
        return f"Plan: {self.nombre_plan}"

# 3. HERENCIA SIMPLE: Multimedia hereda de Servicio
class Multimedia(Servicio):
    def __init__(self, nombre_plan, calidad):
        super().__init__(nombre_plan) # super() llama al abuelo
        self.calidad = calidad

    def reproducir(self):
        return "Reproduciendo contenido estándar..."

# 4. CLASE PARA HERENCIA MÚLTIPLE: Funciones de descarga
class Descargable:
    def __init__(self, limite_descargas):
        self.limite_descargas = limite_descargas

    def descargar(self):
        return f"Descargando... (Cupo restante: {self.limite_descargas} archivos)"

# 5. HERENCIA MULTINIVEL + MÚLTIPLE + POLIMORFISMO
class PlanPremium(Multimedia, Descargable):
    def __init__(self, nombre_plan, calidad, limite_descargas, bono_extra):
        # Inicializamos ambas ramas de la familia
        Multimedia.__init__(self, nombre_plan, calidad)
        Descargable.__init__(self, limite_descargas)
        self.bono_extra = bono_extra

    # POLIMORFISMO: El plan premium reproduce de forma distinta
    def reproducir(self):
        # Usamos super() para obtener la lógica base y añadirle algo más
        base = super().reproducir()
        return f"{base} ¡En 4K Ultra HD con {self.bono_extra}!"

# --- PRUEBA DEL SISTEMA ---
print("--- BIENVENIDO A STREAMMASTER ---")
mi_suscripcion = PlanPremium("Familiar", "4K", 50, "Dolby Atmos")

print(mi_suscripcion.obtener_info())   # Viene del abuelo (Servicio)
print(mi_suscripcion.descargar())      # Viene del padre 2 (Descargable)
print(mi_suscripcion.reproducir())     # Polimorfismo: versión Premium