print("programa en Python que almacene la edad de 5 personas. Al final mostrar por pantalla la menor y mayor edad registrada")
cont = 1
listEdad = []

while cont <= 5:
    edad = int(input("Por favor, introduzca su edad: "))
    listEdad.append(edad)
    cont = cont + 1

for i in range(1,len(listEdad)):
    for posicion in range(len(listEdad) - i):
        if listEdad[posicion] > listEdad[posicion + 1]:
            temp = listEdad[posicion]
            listEdad[posicion] = listEdad[posicion + 1]
            listEdad[posicion + 1] = temp

print(f"La menor edad ingresada es: {listEdad[0]}, la mayor edad es: {listEdad[-1]}")