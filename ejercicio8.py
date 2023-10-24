print("imprima las tablas de multiplicar del 5, 6 7 8 y 9.")

num = [5,6,7,8,9]

for i in num:
    print("")
    print(f"Tabla del {i}")
    for x in range(11):
        result = i * x
        print("{} x {} = {}".format(i,x,result))
        

        