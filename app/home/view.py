from app import app
from flask import render_template

@app.route('/')  
def base():  
    return render_template('home/base.html')

@app.route('/home')  
def home():  
    return render_template('home/home.html')

