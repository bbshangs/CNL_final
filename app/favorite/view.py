from app import app
from flask import render_template
from app.user.model import UserRegister

@app.route('/favorite')  
def favorite():  
    return render_template('favorite/favorite.html')

