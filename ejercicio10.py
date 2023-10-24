# Hacer un programa que calcule el factorial de un número teniendo en cuenta la siguiente
# formula:
# 𝑛! = 𝑛 ∗ (𝑛 − 1)!
# 0! = 1
# 1! = 1
# Ejemplo : 5! = 5 * 4 * 3 * 2 * 1

fact = int(input("Escribe el numero factorial: ")) 

resul = 1

for i in range(1,fact+1):
    op = resul * i
    op = resul
    resul = op * i

print(f"El resultado de la factorización es: {resul}")
    