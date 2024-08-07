from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email,InputRequired
class RegistroQuejaForm(FlaskForm):
    personal = StringField('Nombres de los responsables')
    descirpcion = TextAreaField('Descripcion de la queja',validators=[DataRequired()])
    email = StringField('Email',validators=[Email('Email invalido'),InputRequired('Porfavor proveea de un email para poder notificarle sobre el estado de la queja01')])
    submit = SubmitField('Enviar')
    