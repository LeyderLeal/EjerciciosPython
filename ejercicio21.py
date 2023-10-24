import math

def areaRectangulo(base, altura):
    return base * altura

def areaTriangulo(base, altura):
    return base * altura / 2

def areaRombo(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2


def areaCirculo(radio):
    return math.pi * radio ** 2

print("El área del triángulo es: ")
print(areaTriangulo(5, 10))

print("El área del rombo es: ")
print(areaRombo(15, 20))

print("El área del rectángulo es: ")
print(areaRectangulo(10, 12))

print("El área del círculo es: ")
print(areaCirculo(18))