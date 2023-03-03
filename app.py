from flask import Flask, render_template, Request
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash

import forms
app=Flask(__name__)
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf = CSRFProtect()

COLORS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'purple': 7,
    'grey': 8,
    'white': 9
}

# Diccionario para convertir tolerancias a porcentajes
TOLERANCES = {
    'gold': 5,
    'silver': 10,
    'ninguna': 20
}

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
        success_message = 'Bienvenido {}'.format(user)
        flash(success_message)

    response=make_response(render_template('cookies.html',form=reg_user))
    if len(datos)>0:
        response.set_cookie('datos_user',datos)

    return  response


"""@app.route("/saludo",methods=['GET','POST'])
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres = valor_cookie.split('@')
    return render_template('saludo.html',nomb=nombres[0])"""



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
    return render_template('PracticaCasillas.html')


@app.route('/generar', methods=['POST'])
def generate():
    num_casillas = int(request.form['numero'])
    return render_template('PracticaCasillasGenerar.html', num_casillas=num_casillas)


@app.route('/resultado', methods=['POST'])
def calculate():

    num_casillas = int(request.form['num_casillas'])
    total = 0
    promedio = 0


    boxes = [int(request.form['num'+str(i)]) for i in range(int(request.form['num_casillas']))]

    min_value = min(boxes)
    max_value = max(boxes)
    average_value = sum(boxes) / len(boxes)
    count_dict = {}

    for i in range(num_casillas):
        num = int(request.form['num'+str(i)])
        total += num
        
    
    for box in boxes:
        if box in count_dict:
            count_dict[box] += 1
        else:
            count_dict[box] = 0

    
    return render_template('PracticaCasillasResultado.html', min_value=min_value, max_value=max_value, average_value=average_value, count_dict=count_dict)

# ------------------------------------------------------------------------------------------------------------

@app.route('/traductor')
def traductor():
    return render_template('Practicatraductor.html')

@app.route('/guardar', methods=['POST'])
def save():
    spanish = request.form.get('spanish')
    english = request.form.get('english')

    if not spanish or not english:
        success_message = 'Por favor Introduzca la palabra y su traduccion'
        flash(success_message)
    else:
        with open('diccionario.txt', 'a') as file:
            file.write(f'{spanish},{english}\n')
    
    return render_template('Practicatraductor.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    language = request.form['language']
    translations = []
    with open('diccionario.txt', 'r') as file:
        for line in file:
            spanish, english = line.strip().split(',')
            if language == 'english' and english == query:
                translations.append(spanish)
            elif language == 'spanish' and spanish == query:
                translations.append(english)


    success_message = 'No Se Encontro la Palabra'
    flash(success_message)

      
    return render_template('Practicatraductor.html', translations=translations)



#----------------------------------------------------------------------------------------------------

@app.route('/resistencia')
def resistencia():
    return render_template('PracticaResistencia.html')

@app.route('/calcularResistencia', methods=['POST'])
def calcularResistencia():
    # Obtener los valores de las bandas y la tolerancia del formulario
    banda1 = request.form.get('banda1')
    banda2 = request.form.get('banda2')
    banda3 = request.form.get('banda3')
    tolerancia = request.form.get('tolerancia')
    
    # Convertir los colores a números
    num1 = COLORS[banda1]
    num2 = COLORS[banda2]
    num3 = COLORS[banda3]
    
    # Calcular el valor de la resistencia
    valor = (num1 * 10 + num2) * 10 * num3

    if tolerancia == 'gold':
        minimo = valor - (valor*.05)
        maximo = valor + (valor*.05)
    elif tolerancia == 'silver':
        minimo = valor - (valor*.10)
        maximo = valor + (valor*.10)        
    # Obtener el porcentaje de la tolerancia
    porcentaje_tolerancia = TOLERANCES[tolerancia]
    
    # Devolver el resultado en la plantilla correspondiente
    return render_template('PracticaResistencia.html', banda1=banda1, banda2=banda2, banda3=banda3, tolerancia=tolerancia, valor=valor, porcentaje_tolerancia=porcentaje_tolerancia,maximo=maximo,minimo=minimo)


if __name__=="_main_":
    csrf.init_app(app)
    app.run(debug=True)