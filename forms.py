from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField
from wtforms import validators


def mi_validacion(form,field):
    if len(field.data)==0 :
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',[
        validators.DataRequired(message='El Campo es Requerido'),
        validators.length(min=4,max=8, message='No cumple la longitud esperada')
        ])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El Campo es Requerido')
        ])
    apaterno=StringField('Apaterno',[mi_validacion])
    email = EmailField('correo')


class loginForm(Form):
    username=StringField('usuario',[
        validators.DataRequired(message='El Campo es Requerido'),
        validators.length(min=4,max=8, message='No cumple la longitud esperada')
        ])
    password = StringField('password',[
        validators.DataRequired(message='El Campo es Requerido'),
        validators.length(min=4,max=8, message='No cumple la longitud esperada')
        ])
