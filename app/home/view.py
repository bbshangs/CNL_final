from app import app
from flask import render_template
from app.user.model import UserRegister

@app.route('/')  
def base():  
    return render_template('home/base.html')

@app.route('/home/<user>')  
def home(user):
    return render_template('home/home.html', user=user)
