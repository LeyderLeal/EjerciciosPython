listAprendiz = []
nombre = ""
col,i = 2,0

while nombre != False:
    for j in range(0,col):
        if j == 0:
            nombre = input("Por favor, introduzca su nombre (escriba * para salir): ")
            if nombre == "*":
                nombre = False
                break
            listAprendiz.append([])  
            listAprendiz[i].append(nombre)
        if j == 1:
            edad = int(input("Por favor, introduzca su edad: "))
            listAprendiz[i].append(edad)
    i = i + 1    

print("Alumnos mayores de edad")
for i in range(len(listAprendiz)):
    if listAprendiz[i][1] >= 18:
        print(listAprendiz[i])

print("Alumnos con la mayor edad")
maxEdad = 0
oldest_students = []

for i in listAprendiz:
    if i[1] > maxEdad:
        maxEdad = i[1]

oldest_students = [alumno for alumno in listAprendiz if alumno[1] == maxEdad]
print(oldest_students)        


