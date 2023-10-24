# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y
# posterior ordene los elementos de menor a mayor.
from random import *

listAleatorio = [randint(0, 100) for i in range(10)]

print(listAleatorio)

for i in range(1,len(listAleatorio)):
    for posicion in range(len(listAleatorio) - i):
        if listAleatorio[posicion] > listAleatorio[posicion + 1]:
            temp = listAleatorio[posicion]
            listAleatorio[posicion] = listAleatorio[posicion + 1]
            listAleatorio[posicion + 1] = temp

print(listAleatorio)