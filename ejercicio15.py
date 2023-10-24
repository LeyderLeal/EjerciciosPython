op = 1
wordList = []
interseccion = []

while op == 1:
    palabra = input("Ingrese una palabra: ")
    wordList.append(palabra)
    op = int(input("¿Quiere ingresar otra palabra? 1.Si  2.No: "))

for i in wordList:
    for x in wordList:
        if i == x and i not in interseccion:
            interseccion.append(i)
            
print(interseccion)
    
        


