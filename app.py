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


@app.route("/practica")
def practica():
    return render_template("practica.html")


# ------------------------------------------------------------------------------------------

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    numeroCajas = request.form.get("txtNumero")
    if request.method == 'POST':
        print(numeroCajas)
    return render_template("resultado.html",numeroCajas=numeroCajas)


if __name__=="_main_":
    app.run(debug=True)