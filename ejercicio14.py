print("programa que permite crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista")

op=1
veces = 0
wordList = []

while op == 1:
    palabra = input("Ingrese una palabra: ")
    wordList.append(palabra)
    op = int(input("¿Quiere ingresar otra palabra? 1.Si  2.No: "))

palabraa = input("Ingrese una palabra y le diremos cuantas veces aparece en la lista: ")

for i in wordList:
    if i == palabraa:
        veces += 1
    
print(f"La palabra que ingreso esta {veces} veces escrita en la lista")