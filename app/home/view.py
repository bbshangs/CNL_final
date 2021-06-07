from app import app
from flask import render_template
from app.user.model import UserRegister

@app.route('/', methods=['GET', 'POST'])
def base():  
    return render_template('home/base.html')

@app.route('/home/<user_id>', methods=['GET', 'POST'])  
def home(user_id):
    user = UserRegister.query.filter_by(id=user_id).first()
    user.add_favorite("shiba")
    return render_template('home/home.html', user_id=user_id)
