def triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

def trianguloRectangulo(a, b, c):
    if triangulo(a, b, c):
        lados = [a, b, c]
        hipotenusa = max(lados)
        lados.remove(hipotenusa)
        if lados[0]**2 + lados[1]**2 == hipotenusa**2:
            return True
    return False

a = int(input("ingrese un numero para uno de los lados: "))
b = int(input("ingrese un numero para uno de los lados: "))
c = int(input("ingrese un numero para uno de los lados: "))
if triangulo(a, b, c):
    print("Los lados {}, {} y {} forman un triángulo.".format(a, b, c))
    if trianguloRectangulo(a, b, c):
        print("El triángulo es un triángulo rectángulo.")
    else:
        print("El triángulo no es un triángulo rectángulo.")
else:
    print("Los lados {}, {} y {} no forman un triángulo.".format(a, b, c))