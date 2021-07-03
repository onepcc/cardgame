from Clases.carta import Carta

class Unidad(Carta):
    def __init__(self, nombre,costo,poder=20, resistencia=50):
        super().__init__(nombre,costo)
        self.poder = poder
        self.res = resistencia
    
    def ataca(self,objetivo):
        if self.__class__.__name__== "Unidad":
            if objetivo.res > 0:
                objetivo.res -= self.poder
            return f"""La {self.__class__.__name__} {self.nombre.upper()} ha atacado a : {objetivo.nombre.upper()} por {self.poder} puntos,
            la resistencia de {objetivo.nombre.upper()} ahora es {objetivo.res} """
        else:
            return "No es una Unidad valida"
        
    
    def __str__(self):
        """ Informacion del unidad """
        if self.res < 0:
            return f"La {self.__class__.__name__} {self.nombre} ha muerto"
        else:
            return f"La {self.__class__.__name__} {self.nombre}: cuesta {self.costo} y tiene {self.poder} poder y {self.res} de resistencia"

