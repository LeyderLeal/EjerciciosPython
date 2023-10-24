# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El
# programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el
# cliente es menor de 5 años puede entrar gratis, si tiene entre 5 y 18 años debe pagar 5 mil pesos
# y si es mayor de 18 años debe pagar 10 mil pesos.

edad = int(input("Cual es su edad: "))

if edad > 0:
    if edad < 5:
        print("entre gratis si cree que eso vale su hijo")
    elif edad in range(5,19):
        print("pague 5 mil")
    elif edad > 18:
        print("pague 10 mil")
else:
    print("edad invalida")