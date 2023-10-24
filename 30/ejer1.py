class Perro():
    
    def __init__(self,nombre=None,raza=None):
        self.nombre=nombre
        self.raza=raza
        
    def ladrar(self):
        print(f"{self.nombre} está ladrando")
        
    def caminar(self, pasos):
        print(f"{self.nombre} ha realizado {pasos} pasos")
        
miPerro = Perro("Tango","Beagle")

print(miPerro.nombre)

miPerro.ladrar()

miPerro.caminar(6)

miPerro.nombre = "Apolo"

miPerro.ladrar()
