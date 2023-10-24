def sumarLista(lista):
    suma = 0
    for numeros in lista:
        suma += numeros
    return suma

numeros = [2,8,56,39,25,5,90,156]
print("La suma de la lista es: ")
print(sumarLista(numeros))