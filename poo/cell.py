class Dispositivo:
    def __init__(self, marca):
        self.marca = marca
        self.__encendido = False
        
    def encender(self):
        self.__encendido = True
        return f"{self.marca} encendido."
    
class Telefono (Dispositivo):
    def __init__(self, marca, numero):
        super().__init__(marca)
        # Dispositivo.__init__(self,marca)
        self.numero = numero
        
    def hacer_llamada(self, contacto):
        return f"llamada a {contacto} desde el {self.numero}...."
    
class Camara:
    def __init__(self, megapixeles):
        self.megapixeles = megapixeles;
        
    def tomar_foto(self):
        return f"WISSSSSKI. Foto capturada en {self.megapixeles}MP."
    
    
class Smartphone(Telefono, Camara):
    def __init__(self, marca, numero, megapixeles, modelo):
        Telefono.__init__(self, marca, numero)
        Camara.__init__(self,megapixeles)
        self.modelo = modelo
        
    def encender(self):
        estado_base = super().encender()
        return f"{estado_base} Cargando mi Androide... Bienvenido al {self.modelo}"
    
    
mi_celular = Smartphone("Tecno Sport", "849-433-0448", 500, "Pro MAXIMA")

print(mi_celular.hacer_llamada("Juan MOreno"))
print(mi_celular.encender())
print(mi_celular.tomar_foto())