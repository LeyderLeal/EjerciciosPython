print("programa que lee un número entero y como resultado informa si el número es primo o no.")

num = int(input("Ingrese un numero: "))
cont = 1

if num <=1:
    print("El numero que ingreso no es primo")
elif num != 2:
    if num != 1:
        for i in range(1,num):
            if num % i == 0:
                cont = cont + 1
        if cont == 2:
            print("El numero es primo")
        else:
            print("el numero no es primo")
    else:
        print("El numero no es primo")
elif num == 2:
    print("El numero es primo")