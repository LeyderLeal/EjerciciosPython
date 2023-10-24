nombre = input("Ingrese su nombre: ")
sexo = input("ingrese M para masculino o F para femenino: ")

nombree = nombre.upper()
sexoo = sexo.upper()

if nombree <= "M" and sexoo == "F" or nombree >= "N" and sexoo == "M":
    print("Perteneces al grupo A")  
else:
    print("Perteneces al grupo B")