from animal import Animal

class Perro(Animal):
    
    def __init__(self, peso):
        super().__init__(peso)
        
    def respirar(self):
        print(f"Un {type(self).__name__} Respirando...")
    