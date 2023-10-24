def bisiesto(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def obtenerDiasMes(mes: int, year: int) -> int:
    
    if mes in [4, 6, 9, 11]:
        return 30
    
    if mes == 12:
        if bisiesto(year):
            return 29
        else:
            return 28
    else:
        
        return 31
    
mes = 2
year = 2019
dias = obtenerDiasMes(mes, year)
print("numero de dias en",mes, "de",year)
print(dias)