from flask import Flask, render_template
from flask import request

import forms
app=Flask(__name__)

@app.route("/formulario",methods=['GET','POST'])
def formulario():
    return render_template('formulario.html')

# ------------------------------------------------------------------------------------------

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method=='POST':
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template('alumnos.html', form= alum_form)


# ------------------------------------------------------------------------------------------


@app.route('/')
def index():
    return render_template('practica.html')


@app.route('/generar', methods=['POST'])
def generate():
    num_casillas = int(request.form['numero'])
    return render_template('generar.html', num_casillas=num_casillas)


@app.route('/resultado', methods=['POST'])
def calculate():
    num_casillas = int(request.form['num_casillas'])
    total = 0
    multiplicacion = 1
    promedio = 0


    for i in range(num_casillas):
        num = int(request.form['num'+str(i)])
        total += num

        
        multiplicacion *= num

        promedio = total / num_casillas  

    
    return render_template('resultado.html', total=total, multiplicacion=multiplicacion, promedio=promedio)

if __name__=="_main_":
    app.run(debug=True)