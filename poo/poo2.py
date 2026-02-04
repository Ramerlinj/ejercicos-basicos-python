class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self._ataque = ataque 
    
    def presentacion(self):
        return f"Soy {self.nombre}, vida: {self.vida}, ataque: {self._ataque}"

class Dioses(Personaje):
    def __init__(self, nombre, vida, ataque, habilidad):
        super().__init__(nombre, vida, ataque)
        self.habilidad = habilidad
        self._ataque += 10
        
    def renacimiento(self):
        return f"{self.nombre} renació con: {self.habilidad} y ataque de {self._ataque}"

humano = Personaje("Juan", 100, 20)
print(humano.presentacion())


zeus = Dioses("Zeus", 500, 100, "Rayo")
print(zeus.presentacion()) 
print(zeus.renacimiento()) 