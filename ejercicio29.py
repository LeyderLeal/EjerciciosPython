class Carro():
    def __init__(self, placa=None, marca=None, modelo=None,color=None):
        self.__placa = placa
        self.marca = marca
        self.__modelo = modelo
        self.color = color
        
    def getPlaca(self):
        return self.__placa
    
    def setPlaca(self,placa):
        self.__placa = placa
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self):
        self.__modelo = modelo
    
    
carro = Carro("qqq123","Mazda",2012,"Rojo")
otroCarro = Carro(modelo=2000)

class Libro():
    def __init__(self, titulo=None,autor=None,numeroPaginas=None) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__numeroPaginas = numeroPaginas
        
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self):
        self.__titulo = titulo
    
    def getAutor(self):
        return self.__autor
    
    def setAutor(self):
        self.__autor = autor
    
    def getnumeroPaginas(self):
        return self.__numeroPaginas
    
    def setnumeroPaginas(self):
        self.__numeroPaginas = numeroPaginas

Libro = Libro("El principito","Anonimo",315)