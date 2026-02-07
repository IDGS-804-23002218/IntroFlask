from wtforms import Form, RadioField

from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField

from wtforms import validators

class UserForm(Form):
    matricula = IntegerField("Matricula", {
        validators.DataRequired(message="El campo es requerido")
    })
    nombre = StringField("Nombre", {
        validators.DataRequired(message="El campos es requerido")
    })
    apellido = StringField("Apellido", {
        validators.DataRequired(message="El campos es requerido")
    })
    correo = EmailField("Correo", {
        validators.Email(message="Ingrese Correo valido")
    })
    
class CinepolisForm(Form):
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido"),
        validators.length(min=3, max=10, message="Ingrese un nombre valido")
    ])
    compradores = IntegerField('Cantidad Compradores',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor valido")
        ])
    cineco = RadioField('Es Cineco', choices=[('no','No'),('si','Si')])
    boletos = IntegerField('Cantidad Boletos',[
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor valido")
        ])