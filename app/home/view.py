from app import app
from flask import render_template
from app.user.model import UserRegister
from app.restaurant.model import Restaurant

@app.route('/', methods=['GET', 'POST'])
def base():  
    return render_template('home/base.html')

@app.route('/home/<user_id>', methods=['GET', 'POST'])  
def home(user_id):
    user = UserRegister.query.filter_by(id=user_id).first()

    cheap_restaurant = Restaurant.query.filter_by(price_level=1).all()

    return render_template(
        'home/home.html', 
        user_id=user_id,
        cheap_restaurant=cheap_restaurant
    )
