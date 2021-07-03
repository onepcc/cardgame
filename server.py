from flask import Flask, render_template
from Clases.unidad import Unidad 
from Clases.hechizos import Hechizo 


app = Flask(__name__)

unidad1 = Unidad("Ninja Rojo",3,3,4)
unidad2 = Unidad("Ninja Negro",4,5,4)

algduro = Hechizo("Algoritmo Duro",2,True,3)
promesa = Hechizo("Promesa no manejada",1,True,-2)
pareja = Hechizo("Programacion en pareja",3,False,2)


objeto = []
# El jugador 1 convoca a "Ninja Cinturón Rojo"
player1="JUGADOR 1 juega:"
player2="JUGADOR 2 juega:"

jug1=str(unidad1)
objeto.append(jug1)

# El jugador 1 juega "Algoritmo duro" en "Ninja Cinturón Rojo"
jug2=algduro.lanzar(unidad1)
objeto.append(jug2)
jug2b=str(unidad1)
objeto.append(jug2b)

# El jugador 2 convoca a "Ninja Cinturón Negro"
jug3=str(unidad2)
objeto.append(jug3)

#El jugador 2 juega "Rechazo de promesa no controlada" en "Ninja Cinturón Rojo"
jug4=promesa.lanzar(unidad1)
objeto.append(jug4)
jug4b=str(unidad1)
objeto.append(jug4b)

#El jugador 1 juega "Programación en pareja" en "Ninja Cinturón Rojo"
jug5=pareja.lanzar(unidad1)
objeto.append(jug5)
jug5b=str(unidad1)
objeto.append(jug5b)

#El jugador 1 juega el ataque "Ninja Cinturón Rojo" "Ninja Cinturón Negro"
unidad1.ataca(unidad2)
txt5=unidad1.ataca(unidad2)
objeto.append(txt5)
muerto= str(unidad2)


@app.route("/")
def hello_world2():
    return render_template('index.html', objetos=objeto, over = muerto)

@app.route("/hack")
def hackathon():
    return render_template('index2.html', objetos=objeto, over = muerto)

app.run()