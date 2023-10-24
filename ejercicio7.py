# Hacer un programa que lea un número entero y como resultado mostrar su correspondiente en
# notación binaria.

decimal = int(input("Ingrese un numero entero: "))
num = decimal
binario = ""

while num // 2 != 0:
    binario = str(num%2) + binario
    num = num // 2
    
print(f"El numero {decimal} a binario es {str(num)+binario}")
