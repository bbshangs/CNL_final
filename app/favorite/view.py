from app import app
from flask import render_template
from app.user.model import UserRegister
from app.restaurant.model import Restaurant

@app.route('/favorite/<user_id>', methods=['GET', 'POST']) 
def favorite(user_id):
    user = UserRegister.query.filter_by(id=user_id).first()
    favorite_list = user.get_favorite().split()

    restaurant_list = []
    for favorite in favorite_list:
        restaurant = Restaurant.query.filter_by(place_id=favorite).first()
        restaurant_list.append(restaurant)                                
    return render_template('favorite/favorite.html',
                user_id=user_id, restaurant_list=restaurant_list)

