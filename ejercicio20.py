from datetime import datetime
import os


cuentas_creadas = 0

def __init__(self, identificacion, nombre, correo):
    self.identificacion = identificacion
    self.nombre = nombre
    self.correo = correo
    self.codigo = f"{datetime.now().year}-{CuentaAhorros.cuentas_creadas+1}"
    self.fecha_creacion = datetime.now()
    self.saldo = 0
    CuentaAhorros.cuentas_creadas += 1
    
def consignar(self, valor):
    self.saldo += valor
    
def retirar(self, valor):
    if valor > self.saldo:
        print("No hay suficientes fondos en la cuenta.")
    else:
        self.saldo -= valor
    
def __str__(self):
    return f"Cuenta {self.codigo} - Creada el {self.fecha_creacion} - Saldo: {self.saldo}"


cuentas = []

def crear_cuenta():
    identificacion = input("Ingrese identificación del cliente: ")
    nombre = input("Ingrese nombre completo del cliente: ")
    correo = input("Ingrese correo electrónico del cliente: ")
    cuenta = CuentaAhorros(identificacion, nombre, correo)
    BancoADSO.cuentas.append(cuenta)
    print(f"Cuenta creada exitosamente. Código: {cuenta.codigo}")
    
def consignar_cuenta():
    codigo = input("Ingrese el código de la cuenta a consignar: ")
    cuenta = self.buscar_cuenta(codigo)
    if cuenta:
        valor = float(input("Ingrese el valor a consignar: "))
        cuenta.consignar(valor)
        print(f"Consignación exitosa. Nuevo saldo: {cuenta.saldo}")
    else:
        print("Cuenta no encontrada.")
    
def retirar_cuenta():
    codigo = input("Ingrese el código de la cuenta a retirar: ")
    cuenta = self.buscar_cuenta(codigo)
    if cuenta:
        valor = float(input("Ingrese el valor a retirar: "))
        cuenta.retirar(valor)
        print(f"Retiro exitoso. Nuevo saldo: {cuenta.saldo}")
    else:
        print("Cuenta no encontrada.")
        
def consultar_cuenta_por_codigo():
    codigo = input("Ingrese el código de la cuenta a consultar: ")
    cuenta = self.buscar_cuenta(codigo)
    if cuenta:
        print(cuenta)
    else:
        print("Cuenta no encontrada.")
        
def consultar_cuenta_por_identificacion():
    identificacion = input("Ingrese la identificación del cliente: ")
    cuentas = [cuenta for cuenta in BancoADSO.cuentas if cuenta.identificacion == identificacion]
    if cuentas:
        for cuenta in cuentas:
            print(cuenta)
    else:
        print("No se encontraron cuentas asociadas a la identificación ingresada.")
        
def listar_cuentas():
    for cuenta in BancoADSO.cuentas:
        print(cuenta)
        
def buscar_cuenta(self, codigo):
    for cuenta in BancoADSO.cuentas:
        if cuenta.codigo == codigo:
            return cuenta
    return None
    
def menu():
    while(True):
        os.system("cls")
        print("MENÚ BANCO ADSO 2449133")
        print("1. Crear Cuenta")
        print("2. Consignar Cuenta")
        print("3. Retirar Cuenta")
        print("4. Consultar Cuenta Por Código") 
        print("5. Consultar Cuenta por Identificación Cliente") 
        print("6. Listar Cuentas") 
        print("7. Salir")
        opcion = int(input("Ingrese Opción (1-7):"))
        
        if(opcion==1):
            crear_cuenta()
        elif(opcion==2):
            consignar_cuenta()
        elif(opcion==3):
            retirar_cuenta()
        elif(opcion==4):
            consultar_cuenta_por_codigo()
        elif(opcion==5):
            consultar_cuenta_por_identificacion()
        elif(opcion==6):
            listar_cuentas
        elif(opcion==7):
            print("Va a salir")
            break
        else:
            print("Opción no valida...")
            
        input("Presione enter para continuar")
            
menu()