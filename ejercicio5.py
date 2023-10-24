print("programa que imprime los números múltiplos de 3 que hay entre dos números.")

num1 = int(input("Escriba el primer numero: "))
num2 = int(input("Escriba el segundo numero: "))

for i in range(num1,num2+1):
    coc = i%3
    if coc == 0:
        print(i)
    