from Clases.carta import Carta
from Clases.unidad import Unidad

class Hechizo(Carta):
    def __init__(self, nombre,costo, tipo,magnitud=1):
        super().__init__(nombre,costo)
        self.tipo = tipo
        self.magnitud = magnitud
    
    def lanzar(self,objetivo):
        if objetivo.__class__.__name__== "Unidad":
            if self.tipo == True and objetivo.res >0:
                    objetivo.res += self.magnitud
                    return f"Se ha lanzado {self.__class__.__name__} {self.nombre.upper()} a: {objetivo.nombre.upper()}, ahora su resistencia = {objetivo.res}"
            
            elif self.tipo == False and objetivo.poder >0:
                objetivo.poder += self.magnitud
                return f"Se ha lanzado {self.__class__.__name__} {self.nombre.upper()} a: {objetivo.nombre.upper()}, ahora su poder = {objetivo.poder}"
        
        else:
            return "No se puede atacar un hechizo"
        
        
    
    def __str__(self):
        """ Informacion del hechizo """
        return f"La {self.__class__.__name__} cuesta {self.costo} y tiene {self.poder} poder y {self.res} de resistencia"

