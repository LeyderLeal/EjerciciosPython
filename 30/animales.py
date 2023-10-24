from gato import Gato
from perro import Perro

miGato = Gato(4)

miGato.respirar()

tango = Perro(14)

tango.respirar()

print(f"{type(tango).__name__} tiene {tango.getPeso()} kilos de peso")