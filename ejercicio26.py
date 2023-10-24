def paresImpares(lista):
    pares = []
    impares = []

    pares = [n for n in lista if n % 2 == 0]
    
    impares = [n for n in lista if n % 2 != 0]
    pares.sort()
    impares.sort()
    return pares, impares

lista = [265, 2, 0, 56, 17, 40, 78, 79]
pares, impares = paresImpares(lista)
print('Pares: ', pares)
print('Impares: ', impares)