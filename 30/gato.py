from animal import Animal

class Gato(Animal):
    
    def __init__(self, peso):
        super().__init__(peso)
        
    def respirar(self):
        print(f"Un gato negro Respirando...")
    