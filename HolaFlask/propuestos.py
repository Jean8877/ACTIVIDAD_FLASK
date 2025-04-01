from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            x = float(request.form['x'])
            z = float(request.form['z'])
            result = x * z + z + x
        except ValueError:
            result = "Error: Escriba numeros."
    return render_template('ejer1.html', result=result)

##if __name__ == '__main__':




##segundo ejercicio
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    numero = None
    resultado=[]

    if request.method == 'POST':
        try:
            numero = int(request.form['numero'])
            resultado= [(numero, i, numero*i)  for i in range(1, 11)]
        except ValueError:
            tabla = ["Error: Ingrese un número válido."]        

    return render_template('index2.html', resultado=resultado, numero=numero)

##if __name__ == '__main__':
##    app.run(debug=True)




##ejercicio tres

from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    area = None
    figura = None

    if request.method == 'POST':
        figura = request.form['figura']

        try:
            if figura == 'circulo':
                radio = float(request.form['radio'])
                area = math.pi * (radio ** 2)
            
            elif figura == 'cuadrado':
                lado = float(request.form['lado'])
                area = lado ** 2
            
            elif figura == 'triangulo':
                base = float(request.form['base'])
                altura = float(request.form['altura'])
                area = (base * altura) / 2

        except ValueError:
            area = "Error: Ingrese valores numéricos válidos."

    return render_template('index3.html', area=area, figura=figura)

##if __name__ == '__main__':
  ##  app.run(debug=True)