from flask import render_template
from app.restaurant.model import Restaurant
from app.restaurant import app, GOOGLE_MAPS_EMBED_API_KEY

from app import app

import re

@app.route('/test')
def test():
    return render_template('restaurant/test.html')

@app.route('/restaurant/<place_id>')
def restaurant(place_id):
    cur_restaurant = Restaurant.query.filter_by(place_id=place_id).first()

    if cur_restaurant == None:
        return render_template('restaurant/restaurant_not_found.html')

    # handle phone numer
    phone_number_href = "tel:+886-"
    if cur_restaurant.phone_number[1] == '9':
        phone_number_href += cur_restaurant.phone_number[1:].replace(" ", "")
    else:
        phone_number_href += cur_restaurant.phone_number[1] + '-' + cur_restaurant.phone_number[2:].replace(" ", "")
    
    print(phone_number_href)

    # handle period
    restaurant_period = cur_restaurant.period
    restaurant_period = re.split("', '", cur_restaurant.period[1:-1])

    for i in range(len(restaurant_period)):
        restaurant_period[i] = restaurant_period[i].strip().replace("'", "")
    # print(restaurant_period)

    return render_template(
        'restaurant/restaurant.html', 
        GOOGLE_MAPS_EMBED_API_KEY=GOOGLE_MAPS_EMBED_API_KEY, 
        restaurant_name=cur_restaurant.name, 
        restaurant_address=cur_restaurant.address,
        restaurant_phone=cur_restaurant.phone_number,
        restaurant_phone_href=phone_number_href,
        restaurant_period=restaurant_period
    )
