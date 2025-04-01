##importamos Flask
from flask import Flask 
app=Flask(__name__)

##definimos la ruta
@app.route ("/")
def HolaFlask ():
    return"<h1>¡Hola Flask!</h1> <hr>"

##Definimos una segunda ruta 
@app.route("/ruta2")
def ruta2(): 
    return "<strong> estamos en la segunda ruta </strong> <hr>"

##definimos una tercera ruta 
@app.route("/ruta3")
def ruta3(): 
    return "<em> estamos en la segunda ruta </em> <hr>"

##if __name__== "__main__":
    ## el valor true indica que la app se deja en modo debug
  ##  app.run(debug= True)
    


## importamos flask 
from Flask import Flask
app= Flask(__name__)
 ## definimos la ruta principal 
@app.route("/")
def HolaFlask():
    return "<h1> ¡Hola Flask!</h1> <hr>"
## ahora tomamos la segunda ruta y la reemplazamos por el siguiente ejemplo
## 1.) haga un programa que calcule el promedio de notas sabiendo que tienen un 
## 30%, 30% y 40% respectivamente.
@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado=(nota1*30)/100+(nota2*30)/100+(nota3*40)/100
    return f"<h1> El resultado es: {resultado}</h1> <hr>"


##if __name__== "__main__":
    ##El valor true indica que la app se deja en modo debug 
   ## app.run(debug=True)




##tomamos la tercera ruta y la reemplazamos por el siguiente ejemplo 
##2.) un programa que al capturar la edad de una persoa diga si es:
##menor de edad (menor de 18 años)
##Adulto (mayor o igual a 18 años y menor a 60 años)
##Adulto mayor (mayor o igual a 60 años )

@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades (edad=0):
    if edad< 18:
        R="menor de edad"
    elif(edad<60):
        R="Adulto"
    else:
        R="Adulto mayor"
    return f"<h1> la persona es : {R}</h1><hr>"
##if __name__ == "__main__":
## el valor true indica que la app se deja en modo debug
  ##  app.run(debug=True)




##creamos otra ruta realizamos el siguiente ejemplo
##3.) programa que crea arreglos con valores aleatorios
##importamos la libreria numpy si no existe la instalamos con : 
##pip install numpy 
import numpy as np
@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:colmnas>")
@app.route("/arreglos/<int:valores>/<int:colmnas>/<int:filas>")
def arreglos(valores=0, columnas=0, filas=0):
    if filas == 0:
        arreglo=np.random.randint(valores, size= columnas)
    else:
        arreglo=np.random.randint(valores, size= (filas,columnas))
    return f"<h1> el arrglo aleatorio es : {arreglo}</h1><hr>"
##if __name__== "__main__":
    ## el valor true indica que la app se deja en modo debug
  ##  app.run(debug=True)


