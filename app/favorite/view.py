from app import app
from flask import render_template

@app.route('/favorite')  
def favorite():  
    return render_template('favorite/favorite.html')