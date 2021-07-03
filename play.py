from Clases.carta import Carta 
from Clases.unidad import Unidad 
from Clases.hechizos import Hechizo 

unidad1 = Unidad("Ninja Rojo",3,3,4)
unidad2 = Unidad("Ninja Negro",4,5,4)

objeto = []

txt1=str(unidad1)
objeto.append(txt1)
# print(txt1)
algduro = Hechizo("Algoritmo Duro",2,True,3)
promesa = Hechizo("Promesa no manejada",1,True,-2)
pareja = Hechizo("Programacion en pareja",3,False,2)

algduro.lanzar(unidad1)
txt2=algduro.lanzar(unidad1)
objeto.append(txt2)
promesa.lanzar(unidad1)
txt3=promesa.lanzar(unidad1)
objeto.append(txt3)
pareja.lanzar(unidad1)
txt4=pareja.lanzar(unidad1)
objeto.append(txt4)

unidad1.ataca(unidad2)
txt5=unidad1.ataca(unidad2)
objeto.append(txt5)

pareja.lanzar(promesa)
txt6=pareja.lanzar(promesa)
objeto.append(txt6)

for x in objeto:
    print(x)
