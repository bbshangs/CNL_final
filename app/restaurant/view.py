from flask import render_template, request, Response
from app.restaurant.model import Restaurant
from app.restaurant import app, GOOGLE_MAPS_EMBED_API_KEY
from app.user.model import UserRegister

from app import app

import re

@app.route('/<user_id>/restaurant/<place_id>', methods=['GET', 'POST'])
def restaurant(user_id, place_id):
  
    user = UserRegister.query.filter_by(id=user_id).first()
    # print('debug: user = ', user)
    is_favorite = user.is_favorite(place_id)

    cur_restaurant = Restaurant.query.filter_by(place_id=place_id).first()
    if cur_restaurant == None:
        return render_template('restaurant/restaurant_not_found.html')

    # handle phone numer
    phone_number_href = "tel:+886-"
    if cur_restaurant.phone_number[1] == '9':
        phone_number_href += cur_restaurant.phone_number[1:].replace(" ", "")
    else:
        phone_number_href += cur_restaurant.phone_number[1] + '-' + cur_restaurant.phone_number[2:].replace(" ", "")
    
    # handle period
    restaurant_period = cur_restaurant.period
    restaurant_period = re.split("', '", cur_restaurant.period[1:-1])

    for i in range(len(restaurant_period)):
        restaurant_period[i] = restaurant_period[i].strip().replace("'", "")

    return render_template(
        'restaurant/restaurant.html', 
        GOOGLE_MAPS_EMBED_API_KEY=GOOGLE_MAPS_EMBED_API_KEY, 
        restaurant_name=cur_restaurant.name, 
        restaurant_address=cur_restaurant.address,
        restaurant_phone=cur_restaurant.phone_number,
        restaurant_phone_href=phone_number_href,
        restaurant_period=restaurant_period,
        is_favorite=is_favorite,
    )
 
@app.route('/post_sth', methods=['POST'])
def post_sth():
    user_id = request.values['user_id']
    place_id = request.values['place_id']
    print('debug: ', user_id, place_id)
    user = UserRegister.query.filter_by(id=user_id).first()
    print('debug: POST user = ', user)
    if request.values['action'] == 'add':
        print('debug: POST! favorite added')
        user.add_favorite(place_id)
    elif request.values['action'] == 'remove':
        print('debug: POST! favorite removed')
        user.remove_favorite(place_id)
    else:
        print('debug: POST! sth else')
    
    return Response(status=200)