nvl = int(input("Ingrese el numero de niveles: "))
atrc = 1

for e in range(nvl, 0, -1):
    
    for x in range(e):
        print("  ", end="")
    
    
    for y in range(atrc):
        print("* ", end="")

    print()
    atrc+=2
    
nvl2 = int(input("Ingrese el numero de niveles: "))
atrc2 = 1

for ee in range(nvl2, 0, -1):
    
    for xx in range(e):
        print("  ", end="")
    
    
    for yy in range(atrc2):
        print("* ", end="")

    print()
    atrc2 +=1

