salario = int(input("Ingrese su salario: "))

if salario in range(11999999, 15000001):
    impuesto = salario * 0.03
    print("el impuesto que debes pagar es: ",impuesto,"$")
elif salario in range(15000000, 20000001):
    impuesto = salario * 0.05
    print("el impuesto que debes pagar es: ",impuesto,"$")
elif salario in range(20000000, 30000001):
    impuesto = salario * 0.08
    print("el impuesto que debes pagar es: ", impuesto,"$")
elif salario > 30000000:
    impuesto = salario * 0.1
    print("el impuesto que debes pagar es: ",impuesto,"$")
elif salario < 12000000:
    print("no tiene impuestos")
