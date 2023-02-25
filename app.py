from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms
app=Flask(__name__)
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf = CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

@app.route("/cookies",methods=['GET','POST'])
def cookies():
    reg_user = forms.loginForm(request.form)
    datos=''
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        passw=reg_user.password.data
        datos = user+'@'+passw
        success_message = 'Bienvenido prro {}'.format(user)
        flash(success_message)

    response=make_response(render_template('cookies.html',form=reg_user))
    if len(datos)>0:
        response.set_cookie('datos_user',datos)

    return  response


@app.route("/saludo",methods=['GET','POST'])
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres = valor_cookie.split('@')
    return render_template('saludo.html',nomb=nombres[0])



# -----------------------------------------------------------------------------------------

@app.route("/formulario",methods=['GET','POST'])
def formulario():
    return render_template('formulario.html')

# ------------------------------------------------------------------------------------------

@app.route("/Alumnos", methods=['GET','POST'])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method=='POST' and alum_form.validate():
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
    promedio = 0


   


    for i in range(num_casillas):
        num = int(request.form['num'+str(i)])
        total += num


        promedio = total / num_casillas  

    
    return render_template('resultado.html', minimo=minimo ,promedio=promedio)

if __name__=="_main_":
    csrf.init_app(app)
    app.run(debug=True)