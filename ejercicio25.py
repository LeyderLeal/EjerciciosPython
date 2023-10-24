def calcularTotalIva(cantidadSinIva, porcentajeIva=19):
    totalConIva = cantidadSinIva + cantidadSinIva * (porcentajeIva / 100)
    return totalConIva

print(calcularTotalIva(50000),(10))
print(calcularTotalIva(50000))