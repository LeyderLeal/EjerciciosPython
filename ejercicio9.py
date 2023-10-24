print("Hacer un programa que lea la edad de 5 personas y para cada una de ellas informar en que fase de vacunación contra el covid es asignado.")

cont = 1
# listaEdad = [] 

# while cont <= 5:    
#     edad = int(input("Por favor, introduzca su edad: "))
#     listaEdad.append(edad)
#     cont = cont + 1

# for i in listaEdad:
#     if i < 18:
#         print("En espera de Autorización")
#     elif i >= 18  and i < 30:
#         print("Fase 5")
#     elif i >= 30  and i < 60: 
#         print("fase 4")
#     elif i >= 60  and i < 70:
#         print("Fase 3")
#     elif i >= 70  and i < 80:
#         print("Fase 2")
#     elif i >= 80:
#         print("Fase 1")
        
while cont <= 5:    
    edad = int(input("Por favor, introduzca su edad: "))
    cont = cont + 1
    
    if edad < 18:
        print("En espera de Autorización")
    elif edad >= 18  and edad < 30:
        print("Fase 5")
    elif edad >= 30  and edad < 60: 
        print("fase 4")
    elif edad >= 60  and edad < 70:
        print("Fase 3")
    elif edad >= 70  and edad < 80:
        print("Fase 2")
    elif edad >= 80:
        print("Fase 1")

print("Gracias:)")