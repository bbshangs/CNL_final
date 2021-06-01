from flask_register import db
from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField

class UserRegister(db.Model):
    __tablename__ = 'UserRgeisters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'username:%s' % (self.username)


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

class 
