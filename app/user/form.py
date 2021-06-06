from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, PasswordField
from app.user.model import UserRegister

class FormRegister(FlaskForm):
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

    def validate_username(self, field):
        if UserRegister.query.filter_by(username=field.data).first():
            raise  validators.ValidationError('UserName already exists') 

class FormLogin(FlaskForm):
    username = StringField('UserName', validators=[
        validators.DataRequired(),
        validators.Length(4, 999)
    ])
    password = PasswordField('PassWord', validators=[
        validators.DataRequired()
    ])
    submit = SubmitField('Log in')
