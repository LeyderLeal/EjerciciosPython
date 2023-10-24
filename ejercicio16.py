# Hacer un programa que cree una tabla bidimensional de longitud 5x15 y la cargue con dos
# únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la
# tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
fil = 5
col = 15

listBi = []

for i in range(0,fil):
    listBi.append([])
    for j in range(0,col):
        if i == 0 or i == 4 or j == 0 or j ==14:    
            listBi[i].append(1)
        else:
            listBi[i].append(0)

for x in range(fil):
    for y in range(col):
        print(listBi[x][y],end=' ')
    print()