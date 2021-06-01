from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField

class FormRegister(Form):
    # 4 <= len(username), len(passwd) <= 999
    username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(4, 999)
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(4, 999),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Register New Account')
 
